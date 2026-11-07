from django.core.management.base import BaseCommand
from shop.models import Category, Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seeds the database with sample products for the tuckshop'

    def handle(self, *args, **kwargs):
        # Create categories
        categories_data = [
            {'name': 'Snacks', 'description': 'Chips, biscuits, and other snacks'},
            {'name': 'Beverages', 'description': 'Soft drinks, juices, and water'},
            {'name': 'Sweets', 'description': 'Candies, chocolates, and lollipops'},
            {'name': 'Bread & Pastries', 'description': 'Bread, rolls, and pastries'},
            {'name': 'Dairy', 'description': 'Milk, cheese, and yogurt'},
            {'name': 'Household', 'description': 'Basic household items'},
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))
        
        # Create products
        products_data = [
            # Snacks
            {'name': 'Simba Chips - Regular', 'category': 'Snacks', 'price': '12.50', 'stock': 50, 'threshold': 15, 
             'description': 'Classic potato chips, lightly salted'},
            {'name': 'Simba Chips - BBQ', 'category': 'Snacks', 'price': '12.50', 'stock': 45, 'threshold': 15,
             'description': 'BBQ flavored potato chips'},
            {'name': 'Nik Naks', 'category': 'Snacks', 'price': '10.00', 'stock': 40, 'threshold': 10,
             'description': 'Crunchy corn snacks'},
            {'name': 'Cheese Curls', 'category': 'Snacks', 'price': '9.50', 'stock': 35, 'threshold': 10,
             'description': 'Cheesy corn puffs'},
            {'name': 'Peanuts - Salted', 'category': 'Snacks', 'price': '8.00', 'stock': 30, 'threshold': 10,
             'description': 'Roasted salted peanuts'},
            
            # Beverages
            {'name': 'Coca-Cola 330ml', 'category': 'Beverages', 'price': '10.00', 'stock': 60, 'threshold': 20,
             'description': 'Classic Coca-Cola'},
            {'name': 'Fanta Orange 330ml', 'category': 'Beverages', 'price': '10.00', 'stock': 55, 'threshold': 20,
             'description': 'Orange flavored soft drink'},
            {'name': 'Sprite 330ml', 'category': 'Beverages', 'price': '10.00', 'stock': 50, 'threshold': 20,
             'description': 'Lemon-lime flavored soft drink'},
            {'name': 'Bottled Water 500ml', 'category': 'Beverages', 'price': '7.00', 'stock': 80, 'threshold': 25,
             'description': 'Still mineral water'},
            {'name': 'Tropika Juice 330ml', 'category': 'Beverages', 'price': '12.00', 'stock': 40, 'threshold': 15,
             'description': 'Tropical fruit juice blend'},
            
            # Sweets
            {'name': 'Bar One Chocolate', 'category': 'Sweets', 'price': '15.00', 'stock': 35, 'threshold': 12,
             'description': 'Caramel and nougat chocolate bar'},
            {'name': 'Astros', 'category': 'Sweets', 'price': '2.00', 'stock': 100, 'threshold': 30,
             'description': 'Small chocolate treats'},
            {'name': 'Lollipops', 'category': 'Sweets', 'price': '1.50', 'stock': 120, 'threshold': 40,
             'description': 'Assorted flavored lollipops'},
            {'name': 'Jelly Tots', 'category': 'Sweets', 'price': '8.00', 'stock': 45, 'threshold': 15,
             'description': 'Fruit flavored jelly sweets'},
            
            # Bread & Pastries
            {'name': 'White Bread Loaf', 'category': 'Bread & Pastries', 'price': '18.00', 'stock': 25, 'threshold': 8,
             'description': 'Fresh white bread loaf'},
            {'name': 'Brown Bread Loaf', 'category': 'Bread & Pastries', 'price': '20.00', 'stock': 20, 'threshold': 8,
             'description': 'Wholesome brown bread'},
            {'name': 'Hot Dog Rolls (6 pack)', 'category': 'Bread & Pastries', 'price': '15.00', 'stock': 18, 'threshold': 6,
             'description': 'Fresh hot dog rolls'},
            
            # Dairy
            {'name': 'Milk 1L', 'category': 'Dairy', 'price': '22.00', 'stock': 30, 'threshold': 10,
             'description': 'Fresh full cream milk'},
            {'name': 'Yoghurt 500g', 'category': 'Dairy', 'price': '18.00', 'stock': 25, 'threshold': 8,
             'description': 'Strawberry flavored yoghurt'},
            {'name': 'Cheese Slices', 'category': 'Dairy', 'price': '25.00', 'stock': 20, 'threshold': 7,
             'description': 'Processed cheese slices'},
            
            # Household
            {'name': 'Toilet Paper (4 rolls)', 'category': 'Household', 'price': '28.00', 'stock': 15, 'threshold': 5,
             'description': 'Soft toilet paper'},
            {'name': 'Matches', 'category': 'Household', 'price': '3.00', 'stock': 40, 'threshold': 10,
             'description': 'Safety matches'},
            {'name': 'Candles (Pack of 10)', 'category': 'Household', 'price': '15.00', 'stock': 22, 'threshold': 7,
             'description': 'White household candles'},
        ]
        
        for prod_data in products_data:
            category = categories[prod_data['category']]
            product, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults={
                    'category': category,
                    'price': Decimal(prod_data['price']),
                    'stock_quantity': prod_data['stock'],
                    'low_stock_threshold': prod_data['threshold'],
                    'description': prod_data['description'],
                    'is_active': True,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
        
        self.stdout.write(self.style.SUCCESS('\nDatabase seeded successfully!'))
        self.stdout.write(self.style.SUCCESS(f'Total Categories: {Category.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Total Products: {Product.objects.count()}'))
