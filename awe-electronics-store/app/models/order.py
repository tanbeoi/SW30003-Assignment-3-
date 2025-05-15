class Order:
    def __init__(self, order_id, customer, products, status="Pending"):
        self.order_id = order_id
        self.customer = customer
        self.products = products  # List of Product objects
        self.status = status
        self.invoice = None
        self.receipt = None
        self.shipping_details = None

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def generate_invoice(self):
        # Logic to generate invoice
        pass

    def generate_receipt(self):
        # Logic to generate receipt
        pass

    def update_status(self, new_status):
        self.status = new_status

    def set_shipping_details(self, shipping_details):
        self.shipping_details = shipping_details

    def get_order_summary(self):
        return {
            "order_id": self.order_id,
            "customer": self.customer,
            "products": [product.get_details() for product in self.products],
            "status": self.status,
            "shipping_details": self.shipping_details,
            "invoice": self.invoice,
            "receipt": self.receipt,
        }