class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def browse_store(self):
        # Logic for browsing the store
        pass

class Customer(Person):
    def __init__(self, name, email):
        super().__init__(name, email)

    def place_order(self):
        # Logic for placing an order
        pass

    def create_account(self):
        # Logic for creating an account
        pass

    def view_order_status(self):
        # Logic for viewing order status
        pass

class TeamMember(Person):
    def __init__(self, name, email):
        super().__init__(name, email)

    def view_customer_orders(self):
        # Logic for viewing customer orders
        pass

    def update_order_status(self):
        # Logic for updating order status
        pass

    def adjust_stock(self):
        # Logic for adjusting stock
        pass

    def view_sales_data(self):
        # Logic for viewing sales data
        pass