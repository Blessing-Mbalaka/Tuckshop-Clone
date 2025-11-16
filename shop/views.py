from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Order, LineItem
import uuid

# Create your views here.

def home(request):
    """Home page with featured products"""
    products = Product.objects.filter(is_active=True)[:8]
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop/home.html', context)


def product_list(request):
    """List all products with filtering"""
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
    
    # Search
    search = request.GET.get('search')
    if search:
        products = products.filter(
            Q(name__icontains=search) | 
            Q(description__icontains=search)
        )
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': category_id,
        'search_query': search,
    }
    return render(request, 'shop/product_list.html', context)


def product_detail(request, pk):
    """Product detail page"""
    product = get_object_or_404(Product, pk=pk, is_active=True)
    
    context = {
        'product': product,
    }
    return render(request, 'shop/product_detail.html', context)


@login_required
def add_to_cart(request, pk):
    """Add product to cart (session-based)"""
    product = get_object_or_404(Product, pk=pk, is_active=True)
    
    # Get or create cart in session
    cart = request.session.get('cart', {})
    
    product_id = str(pk)
    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': 1,
        }
    
    request.session['cart'] = cart
    messages.success(request, f'{product.name} added to cart!')
    
    return redirect('product_list')


@login_required
def cart_view(request):
    """View shopping cart"""
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    
    for product_id, item_data in cart.items():
        product = get_object_or_404(Product, pk=int(product_id))
        subtotal = float(item_data['price']) * item_data['quantity']
        total += subtotal
        
        cart_items.append({
            'product': product,
            'quantity': item_data['quantity'],
            'price': item_data['price'],
            'subtotal': subtotal,
        })
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'shop/cart.html', context)


@login_required
def update_cart(request, pk):
    """Update cart item quantity"""
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        product_id = str(pk)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > 0:
            if product_id in cart:
                cart[product_id]['quantity'] = quantity
                messages.success(request, 'Cart updated!')
        else:
            if product_id in cart:
                del cart[product_id]
                messages.success(request, 'Item removed from cart!')
        
        request.session['cart'] = cart
    
    return redirect('cart_view')


@login_required
def remove_from_cart(request, pk):
    """Remove item from cart"""
    cart = request.session.get('cart', {})
    product_id = str(pk)
    
    if product_id in cart:
        del cart[product_id]
        messages.success(request, 'Item removed from cart!')
    
    request.session['cart'] = cart
    return redirect('cart_view')


@login_required
def checkout(request):
    """Process checkout and create order"""
    cart = request.session.get('cart', {})
    
    if not cart:
        messages.error(request, 'Your cart is empty!')
        return redirect('product_list')
    
    # Create order
    order = Order.objects.create(
        user=request.user,
        reference=f'ORD-{uuid.uuid4().hex[:8].upper()}',
        status='pending'
    )
    
    # Create line items
    for product_id, item_data in cart.items():
        product = get_object_or_404(Product, pk=int(product_id))
        
        # Check stock
        if product.stock_quantity < item_data['quantity']:
            messages.error(request, f'Not enough stock for {product.name}')
            order.delete()
            return redirect('cart_view')
        
        LineItem.objects.create(
            order=order,
            product=product,
            quantity=item_data['quantity'],
            price=product.price
        )
        
        # Update stock
        product.stock_quantity -= item_data['quantity']
        product.save()
    
    # Calculate total
    order.calculate_total()
    order.save()
    
    # Clear cart
    request.session['cart'] = {}
    
    messages.success(request, f'Order {order.reference} created successfully!')
    return redirect('order_detail', pk=order.pk)


@login_required
def order_list(request):
    """List user's orders"""
    if request.user.is_staff:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user=request.user)
    
    context = {
        'orders': orders,
    }
    return render(request, 'shop/order_list.html', context)


@login_required
def order_detail(request, pk):
    """Order detail page"""
    if request.user.is_staff:
        order = get_object_or_404(Order, pk=pk)
    else:
        order = get_object_or_404(Order, pk=pk, user=request.user)
    
    context = {
        'order': order,
    }
    return render(request, 'shop/order_detail.html', context)


@login_required
def update_order_status(request, pk):
    """Update order status (staff only)"""
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to perform this action.')
        return redirect('order_list')
    
    order = get_object_or_404(Order, pk=pk)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            messages.success(request, f'Order {order.reference} status updated to {order.get_status_display()}')
    
    return redirect('order_detail', pk=pk)
