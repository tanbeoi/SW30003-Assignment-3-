# AWE Electronics Store

AWE Electronics is an online electronics store that aims to expand its customer base across Australia. This project implements a web application that automates the order and payment process while providing functionalities to manage stock, user accounts, and sales data.

## Project Structure

```
awe-electronics-store
├── app
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── account.py
│   │   ├── database.py
│   │   ├── order.py
│   │   ├── payment.py
│   │   ├── person.py
│   │   └── product.py
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── account_controller.py
│   │   ├── order_controller.py
│   │   ├── product_controller.py
│   │   └── team_member_controller.py
│   ├── views
│   │   ├── __init__.py
│   │   ├── account_views.py
│   │   ├── order_views.py
│   │   ├── product_views.py
│   │   └── team_member_views.py
│   ├── static
│   │   ├── css
│   │   ├── js
│   │   └── img
│   └── templates
│       ├── base.html
│       ├── account
│       ├── orders
│       ├── products
│       └── team_member
├── data
│   ├── accounts.json
│   ├── orders.json
│   └── products.json
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Features

- **User Management**: Create and manage user accounts.
- **Product Management**: Add, update, and view products in stock.
- **Order Processing**: Place orders, view order status, and manage invoices and receipts.
- **Sales Data**: Authorized team members can view sales data and analytics.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd awe-electronics-store
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python run.py
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

