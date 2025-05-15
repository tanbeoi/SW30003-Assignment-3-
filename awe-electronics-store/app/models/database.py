class Database:
    def __init__(self, accounts_file='data/accounts.json', orders_file='data/orders.json', products_file='data/products.json'):
        self.accounts_file = accounts_file
        self.orders_file = orders_file
        self.products_file = products_file
        self.load_data()

    def load_data(self):
        self.accounts = self._load_json(self.accounts_file)
        self.orders = self._load_json(self.orders_file)
        self.products = self._load_json(self.products_file)

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

    def get_accounts(self):
        return self.accounts

    def get_orders(self):
        return self.orders

    def get_products(self):
        return self.products

    def find_account(self, account_id):
        return next((account for account in self.accounts if account['id'] == account_id), None)

    def find_order(self, order_id):
        return next((order for order in self.orders if order['id'] == order_id), None)

    def find_product(self, product_id):
        return next((product for product in self.products if product['id'] == product_id), None)