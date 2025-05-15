class Product:
    def __init__(self, product_id, name, description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def update_stock(self, quantity):
        self.quantity += quantity

    def reduce_stock(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
        else:
            raise ValueError("Insufficient stock available.")

    def get_product_info(self):
        return {
            "id": self.product_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity
        }