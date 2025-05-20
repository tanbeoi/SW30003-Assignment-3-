class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def browse_store(self):
        """
        Logic for browsing the store
        Returns a list of products
        """
        # Get list of products from database 
        from app.models.database import Database
        db = Database()
        return db.get_products()

class Customer(Person):
    def __init__(self, name, email, customer_id=None):
        super().__init__(name, email)
        self.customer_id = customer_id
        self.shopping_cart = []

    def place_order(self, shipping_address=None):
        """
        Create and place an order with the products in the shopping cart
        Requires an active account (customer_id)
        """
        # Check if customer has an account
        if not self.customer_id:
            raise PermissionError("You must create an account before placing an order")
            
        if not self.shopping_cart:
            raise ValueError("Shopping cart is empty")
            
        from app.models.order import Order
        from app.models.database import Database
        
        db = Database()
        
        # Generate unique order ID by counting the number of existing orders then add 1 
        order_id = len(db.get_orders()) + 1
        payment_id = len(db.get_payments()) + 1
        
        # Create new order
        order = {
            "order_id": order_id,
            "account_id": self.customer_id,
            "products": self.shopping_cart,
            "status": "Pending",
            "shipping_address": shipping_address,
            "payment_id": payment_id
        }
        
        # Add to database
        db.add_order(order)
        
        # Clear shopping cart
        self.shopping_cart = []
        
        return order_id

    def add_to_cart(self, product_id, quantity=1):
        """
        Add a product to the shopping cart
        Requires an active account (customer_id)
        """
        # Check if customer has an account
        if not self.customer_id:
            raise PermissionError("You must create an account before adding items to cart")
            
        from app.models.database import Database
        
        db = Database()
        product = next((p for p in db.get_products() if p.get('product_id') == product_id), None)
        
        if not product:
            raise ValueError(f"Product with ID {product_id} not found")
            
        if product.get('stock_quantity', 0) < quantity:
            raise ValueError(f"Insufficient stock for product {product.get('name')}")
            
        cart_item = {
            "product_id": product_id,
            "name": product.get('name'),
            "price": product.get('price'),
            "quantity": quantity,
            "total": product.get('price') * quantity
        }
        
        self.shopping_cart.append(cart_item)
        return self.shopping_cart

    def create_account(self, username, password, is_team_member=False):
        """
        Create a new account for this customer or team member
        """
        from app.models.database import Database
        
        db = Database()
        
        # Generate unique account ID
        account_id = len(db.get_accounts()) + 1
        
        # Create new account
        account = {
            "account_id": account_id,
            "user_name": username,
            "password": password,  # In production, this should be hashed
            "email": self.email,
            "role": "team_member" if is_team_member else "customer",
        }
        
        # Add employee_id for team members
        if is_team_member and hasattr(self, 'employee_id'):
            account["employee_id"] = self.employee_id
        
        # Add to database
        db.add_account(account)
        
        # Update customer with account ID
        self.customer_id = account_id
        
        return account_id

    def view_order_status(self, order_id):
        """
        View the status of a specific order
        """
        from app.models.database import Database
        
        db = Database()
        
        # Find order
        order = next((o for o in db.get_orders() if o.get('order_id') == order_id), None)
        
        if not order:
            raise ValueError(f"Order with ID {order_id} not found")
            
        # Check if customer is authorized to view this order
        if order.get('account_id') != self.customer_id:
            raise PermissionError("Not authorized to view this order")
            
        return {
            "order_id": order.get('order_id'),
            "status": order.get('status'),
            "products": order.get('products', [])
        }

class TeamMember(Customer):
    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.employee_id = employee_id


    def view_customer_orders(self, customer_id=None):
        """
        View all orders or orders for a specific customer
        """
        from app.models.database import Database
        
        db = Database()
        orders = db.get_orders()
        
        # Return all orders of a customer or else return all orders 
        if customer_id:
            orders = [o for o in orders if o.get('account_id') == customer_id]
            
        return orders

    def update_order_status(self, order_id, new_status):
        """
        Update the status of an order
        """
        from app.models.database import Database
        
        db = Database()
        
        # Update order status
        update_data = {"status": new_status}
        result = db.update_order(order_id, update_data)
        
        if not result:
            raise ValueError(f"Order with ID {order_id} not found")
            
        return True

    def adjust_stock(self, product_id, quantity_change):
        """
        Adjust the stock level of a product
        """
        from app.models.database import Database
        
        db = Database()
        
        # Find product
        product = next((p for p in db.get_products() if p.get('product_id') == product_id), None)
        
        if not product:
            raise ValueError(f"Product with ID {product_id} not found")
            
        # Calculate new quantity
        current_quantity = product.get('stock_quantity', 0)
        new_quantity = current_quantity + quantity_change
        
        if new_quantity < 0:
            raise ValueError("Stock quantity cannot be negative")
            
        # Update product
        update_data = {"stock_quantity": new_quantity}
        result = db.update_product(product_id, update_data)
        
        if not result:
            raise ValueError(f"Failed to update product with ID {product_id}")
            
        return new_quantity

    def view_sales_data(self, start_date=None, end_date=None):
        """
        View sales data, optionally filtered by date range
        """
        from app.models.database import Database
        
        db = Database()
        
        # Get all completed orders
        orders = [o for o in db.get_orders() if o.get('status') == 'Completed']
        
        # Calculate total sales
        total_sales = sum(sum(item.get('total', 0) for item in order.get('products', [])) for order in orders)
        
        # Count products sold
        products_sold = {}
        for order in orders:
            for item in order.get('products', []):
                product_id = item.get('product_id')
                quantity = item.get('quantity', 0)
                
                # If this item has been in the product_sold dict, add the quanitty to it
                # Or else, add the product_id to the dict with the quantity 
                if product_id in products_sold:
                    products_sold[product_id] += quantity
                else:
                    products_sold[product_id] = quantity
        
        return {
            "total_sales": total_sales,
            "order_count": len(orders),
            "products_sold": products_sold
        }