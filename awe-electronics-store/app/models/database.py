import json
import os
from pathlib import Path

class Database:
    # Singleton pattern implementation: ensure only one instance of Database exists
    _instance = None
     
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance
     
    def __init__(self, accounts_file=None, orders_file=None, 
             products_file=None, payments_file=None):
        # Skip initialization if already initialized
        if hasattr(self, 'initialized') and self.initialized:
            return
        
        # Get project root directory (parent of app directory)
        project_dir = Path(__file__).parent.parent.parent
        db_dir = os.path.join(project_dir, 'database')
        
        # Use absolute paths by default
        self.accounts_file = accounts_file or os.path.join(db_dir, 'Account.json')
        self.orders_file = orders_file or os.path.join(db_dir, 'Order.json')
        self.products_file = products_file or os.path.join(db_dir, 'Product.json')
        self.payments_file = payments_file or os.path.join(db_dir, 'Payment.json')
        
        # Create directories if they don't exist
        os.makedirs(os.path.dirname(self.accounts_file), exist_ok=True)
        os.makedirs(os.path.dirname(self.orders_file), exist_ok=True)
        os.makedirs(os.path.dirname(self.products_file), exist_ok=True)
        os.makedirs(os.path.dirname(self.payments_file), exist_ok=True)
        
        self.load_data()
        self.initialized = True

    def load_data(self):
        self.accounts = self._load_json(self.accounts_file)
        self.orders = self._load_json(self.orders_file)
        self.products = self._load_json(self.products_file)
        self.payments = self._load_json(self.payments_file)

    def _load_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_data(self):
        self._save_json(self.accounts_file, self.accounts)
        self._save_json(self.orders_file, self.orders)
        self._save_json(self.products_file, self.products)
        self._save_json(self.payments_file, self.payments)

    def _save_json(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def add_account(self, account):
        self.accounts.append(account)
        self.save_data()

    def add_order(self, order):
        self.orders.append(order)
        self.save_data()

    def add_product(self, product):
        self.products.append(product)
        self.save_data()

    def add_payment(self, payment):
        self.payments.append(payment)
        self.save_data()

    def get_accounts(self):
        return self.accounts

    def get_orders(self):
        return self.orders

    def get_products(self):
        return self.products

    def get_payments(self):
        return self.payments

    def find_account(self, account_id):
        return next((account for account in self.accounts if account['id'] == account_id), None)

    def find_order(self, order_id):
        return next((order for order in self.orders if order['id'] == order_id), None)

    def find_product(self, product_id):
        return next((product for product in self.products if product['id'] == product_id), None)

    def find_payment(self, payment_id):
        return next((payment for payment in self.payments if payment.get('payment_id') == payment_id), None)

    def find_payment_by_order(self, order_id):
        return next((payment for payment in self.payments if payment.get('order_id') == order_id), None)

     # I added update and delete methods - Tan
     
    def update_account(self, account_id, updated_data):
        for i, account in enumerate(self.accounts):
            if account.get('account_id') == account_id:
                self.accounts[i].update(updated_data)
                self.save_data()
                return True
        return False
    
    def update_order(self, order_id, updated_data):
        for i, order in enumerate(self.orders):
            if order.get('order_id') == order_id:
                self.orders[i].update(updated_data)
                self.save_data()
                return True
        return False
    
    def update_product(self, product_id, updated_data):
        for i, product in enumerate(self.products):
            if product.get('product_id') == product_id:
                self.products[i].update(updated_data)
                self.save_data()
                return True
        return False

    def update_payment(self, payment_id, updated_data):
        for i, payment in enumerate(self.payments):
            if payment.get('payment_id') == payment_id:
                self.payments[i].update(updated_data)
                self.save_data()
                return True
        return False
    
    def delete_account(self, account_id):
        self.accounts = [a for a in self.accounts if a.get('account_id') != account_id]
        self.save_data()
    
    def delete_order(self, order_id):
        self.orders = [o for o in self.orders if o.get('order_id') != order_id]
        self.save_data()
    
    def delete_product(self, product_id):
        self.products = [p for p in self.products if p.get('product_id') != product_id]
        self.save_data()

    def delete_payment(self, payment_id):
        """Delete a payment record"""
        self.payments = [p for p in self.payments if p.get('payment_id') != payment_id]
        self.save_data()

