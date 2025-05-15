class Account:
    def __init__(self, user_id, name, email, address):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.address = address
        self.order_history = []
        self.shopping_cart = []

    def add_to_cart(self, product):
        self.shopping_cart.append(product)

    def remove_from_cart(self, product):
        if product in self.shopping_cart:
            self.shopping_cart.remove(product)

    def clear_cart(self):
        self.shopping_cart.clear()

    def save_order(self, order):
        self.order_history.append(order)

    def get_order_history(self):
        return self.order_history

    def update_personal_info(self, name=None, email=None, address=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if address:
            self.address = address