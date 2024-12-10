# Factory Management System

A modular factory management system built with Flask, implementing the Factory Application Pattern, Flask Blueprints, and API throttling.

## Features

- Employee Management
- Product Management
- Order Processing
- Customer Management
- Production Tracking
- API Rate Limiting
- Modular Design with Blueprints

## Project Structure

```
.
├── README.md
├── app.py              # Application factory and main entry point
├── config.py           # Configuration settings
├── models.py           # Database models
├── requirements.txt    # Project dependencies
└── blueprints/        # Modular components
    ├── employee.py
    ├── product.py
    ├── order.py
    ├── customer.py
    └── production.py
```

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## API Endpoints

### Employees
- POST /employees - Create a new employee
- GET /employees - List all employees

### Products
- POST /products - Create a new product
- GET /products - List all products

### Orders
- POST /orders - Create a new order
- GET /orders - List all orders

### Customers
- POST /customers - Create a new customer
- GET /customers - List all customers

### Production
- POST /production - Create a new production record
- GET /production - List all production records

## Rate Limiting

The API implements rate limiting with the following default rules:
- 200 requests per day
- 50 requests per hour

## Database

The application uses SQLite as the database. The database file will be created automatically when you run the application for the first time.
