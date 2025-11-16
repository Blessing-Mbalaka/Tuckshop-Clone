# TuckShop Django - Quick Setup Guide

## Prerequisites
- Python 3.8 or higher
- pip package manager

## Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Database Setup
```bash
# Create database tables
python manage.py migrate
```

### 3. Create Admin User
```bash
# Create superuser account
python manage.py createsuperuser
```
Follow the prompts to set:
- Username
- Email address
- Password

### 4. Load Sample Data (Optional)
```bash
# Populate database with sample products
python manage.py seed_data
```

This creates:
- 6 product categories
- 23 sample products with realistic pricing
- Stock levels and low-stock thresholds

### 5. Run Development Server
```bash
python manage.py runserver
```

The application will be available at:
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## First Steps

### For Customers:
1. Navigate to http://127.0.0.1:8000/
2. Click "Register" to create an account
3. Browse products and add items to cart
4. Proceed to checkout to create orders

### For Shop Managers:
1. Login with admin credentials at http://127.0.0.1:8000/admin/
2. Navigate to "Products" to manage inventory
3. Set stock levels and low-stock thresholds
4. View and update order statuses under "Orders"

## Common Tasks

### Adding New Products
1. Go to Admin Panel → Shop → Products → Add Product
2. Fill in product details:
   - Name
   - Category
   - Description
   - Price
   - Stock quantity
   - Low stock threshold
3. Optionally upload product image
4. Save

### Managing Orders
1. Go to Admin Panel → Shop → Orders
2. Click on an order to view details
3. Update status as needed:
   - Pending: New order
   - Processing: Being prepared
   - Completed: Fulfilled
   - Cancelled: Cancelled order

### Monitoring Stock
- Products are highlighted in admin when stock is low
- Low stock = stock quantity ≤ low stock threshold
- Update stock quantities directly in the product list

## Configuration

### Settings
Main settings are in `tuckshop/settings.py`:
- Database configuration
- Static files paths
- Installed apps
- Authentication settings

### Customization
- Templates: `templates/` directory
- Static files: `static/` directory
- Models: `shop/models.py`
- Admin configuration: `shop/admin.py`

## Troubleshooting

### Server won't start
```bash
# Check if port 8000 is in use
lsof -i :8000

# Run on different port
python manage.py runserver 8080
```

### Database errors
```bash
# Reset database (WARNING: deletes all data)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_data
```

### Static files not loading
```bash
# Collect static files
python manage.py collectstatic
```

## Production Deployment

Before deploying to production:

1. Set `DEBUG = False` in settings.py
2. Change `SECRET_KEY` to a unique value
3. Update `ALLOWED_HOSTS` with your domain
4. Use PostgreSQL or MySQL instead of SQLite
5. Configure proper static file serving
6. Set up HTTPS
7. Use environment variables for sensitive data

## Support

For issues or questions:
- Check README.md for detailed documentation
- Review Django documentation: https://docs.djangoproject.com/
- Check the original ASP.NET Core code in `src/` directory for reference

## License

Open source - free for educational and commercial use.
