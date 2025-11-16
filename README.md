# TuckShop - Django Spaza Shop Management System

This is a fully functional Django web application for managing a small spaza shop (tuckshop) with inventory stock control and purchase management capabilities.

## Features

### Customer Features
- **User Registration & Authentication**: Secure account creation and login system
- **Product Catalog**: Browse products by category with search functionality
- **Shopping Cart**: Session-based shopping cart with quantity management
- **Order Management**: Place orders and track order status
- **Responsive Design**: Mobile-friendly interface with modern CSS styling

### Management Features (Staff/Admin)
- **Inventory Management**: 
  - Add, edit, and delete products
  - Track stock levels with low-stock alerts
  - Categorize products for better organization
  - Set low-stock thresholds for automatic monitoring
  
- **Order Processing**:
  - View all customer orders
  - Update order status (Pending, Processing, Completed, Cancelled)
  - Track order history and details
  
- **Admin Dashboard**:
  - Full Django admin interface for comprehensive management
  - Bulk operations on products and orders
  - User management

## Technology Stack

- **Backend**: Django 4.2
- **Database**: SQLite (easily configurable for PostgreSQL/MySQL)
- **Frontend**: Bootstrap 5, Font Awesome icons
- **Forms**: Django Crispy Forms with Bootstrap 4 theme
- **Image Handling**: Pillow

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Blessing-Mbalaka/Tuckshop-Clone.git
   cd Tuckshop-Clone
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set username, email, and password.

5. **Seed the database with sample data (optional)**
   ```bash
   python manage.py seed_data
   ```
   This creates sample categories and products to get started quickly.

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - Login with the superuser credentials you created

## Usage

### For Customers
1. Register for an account or login
2. Browse products from the home page or products page
3. Use the search bar or category filters to find specific items
4. Add products to your cart
5. Review your cart and proceed to checkout
6. View your order history in the Orders section

### For Shop Managers/Staff
1. Login with staff credentials
2. Access the Admin Panel from the navigation menu
3. Manage products:
   - Add new products with details, pricing, and stock levels
   - Update existing product information
   - Monitor low-stock items (highlighted in admin)
4. Process orders:
   - View all customer orders
   - Update order status as they are fulfilled
   - Track order details and items

## Project Structure

```
Tuckshop-Clone/
├── tuckshop/           # Project settings
├── shop/               # Main shop app
│   ├── models.py       # Product, Order, LineItem models
│   ├── views.py        # View logic
│   ├── urls.py         # URL routing
│   └── admin.py        # Admin configuration
├── accounts/           # User authentication app
├── templates/          # HTML templates
│   ├── base.html       # Base template with navigation
│   ├── shop/           # Shop templates
│   └── accounts/       # Auth templates
├── static/             # Static files (CSS, JS, images)
├── media/              # User-uploaded files
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## Models

### Product
- Name, category, description
- Price and stock quantity
- Low stock threshold for alerts
- Image support
- Active/inactive status

### Category
- Name and description
- Groups products for easy browsing

### Order
- Customer reference
- Status tracking (Pending, Processing, Completed, Cancelled)
- Total amount calculation
- Order date and notes

### LineItem
- Links products to orders
- Quantity and price at time of order
- Automatic subtotal calculation

## Enhanced Styling Features

- Modern, responsive design with Bootstrap 5
- Color-coded status badges for orders
- Low-stock visual indicators
- Smooth animations and transitions
- Card-based layout for products
- Gradient backgrounds and shadows
- Mobile-optimized navigation
- Font Awesome icons throughout
- Professional color scheme suitable for a shop environment

## Default Admin Credentials

If you used the automated setup:
- Username: `admin`
- Email: `admin@tuckshop.com`
- Password: `admin123`

**⚠️ Important**: Change these credentials in production!

## Future Enhancements

- Payment gateway integration
- Sales reports and analytics
- Email notifications for orders
- Invoice generation
- Product image galleries
- Customer reviews and ratings
- Barcode scanning for inventory
- Multi-currency support

## License

This project is open source and available for educational and commercial use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Legacy Note

This project was converted from an ASP.NET Core application to Django. The original ASP.NET Core code is preserved in the `src/` directory for reference purposes.
