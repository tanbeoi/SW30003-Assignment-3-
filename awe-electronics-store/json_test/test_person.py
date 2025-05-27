import sys
import os
from pathlib import Path

# Add parent directory to path so we can import our app modules
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

# Import Database first, so when Person classes are imported, they'll use this instance
from app.models.database import Database

# Create a Database instance with default parameters
# It will automatically use absolute paths to the correct database files
db = Database()

# Import Person classes after Database initialization
from app.models.person import Person, Customer, TeamMember

# Clear the database and set up test data
def setup_test_data():
    db.accounts = []
    db.products = [
        {
            "product_id": 1,
            "name": "Viper V3 Pro",
            "description": "Best Gaming Mouse on the market",
            "price": 10.0,
            "stock_quantity": 50
        },
        {
            "product_id": 2,
            "name": "Hyper Light Drifter",
            "description": "Best Indie Game",
            "price": 20.0,
            "stock_quantity": 25
        }
    ]
    db.orders = []
    db.payments = []
    db.save_data()
    return db

def test_all():
    """Run all tests"""
    print("\n=== Running Person class tests ===")
    test_person_class()
    
    print("\n=== Running Customer class tests ===")
    test_customer_class()
    
    print("\n=== Running TeamMember class tests ===")
    test_team_member_class()
    
    print("\nAll tests completed!")

def test_person_class():
    """Test Person class methods"""
    # Setup
    setup_test_data()
    person = Person("Test Person", "test@example.com")
    
    # Test browse_store
    print("Testing browse_store()...")
    products = person.browse_store()
    assert len(products) == 2, "Should return 2 products"
    assert products[0].get('name') == "Viper V3 Pro", "First product name incorrect"
    print("Browse_store() works correctly")


def test_customer_class():
    """Test Customer class methods"""
    # Setup
    setup_test_data()
    customer1 = Customer("Tan", "tanbeoi@gmail.com")
    
    # Test create_account
    print("Testing create_account()...")
    account_id = customer1.create_account("tanbeoi", "12345")
    assert account_id == 1, "First account ID should be 1"
    assert customer1.account_id == account_id, "Customer ID should be set"
    
    accounts = db.get_accounts()
    assert len(accounts) == 1, "Should be 1 account in database"
    assert accounts[0].get('role') == "customer", "Role should be customer"
    print("create_account() works correctly")
    
    # Test add_to_cart
    print("Testing add_to_cart()...")
    cart = customer1.add_to_cart(1, 2)  # Add 2 of product ID 1
    assert len(cart) == 1, "Cart should have 1 item"
    assert cart[0].get('quantity') == 2, "Quantity should be 2"
    assert cart[0].get('total') == 20.0, "Total should be 20.0"
    print("add_to_cart() works correctly")
    
    # Test place_order
    print("Testing place_order()...")
    order_id = customer1.place_order("Swinburne University, John St, Hawthorn, VIC 3122")
    assert order_id == 1, "First order ID should be 1"
    assert len(customer1.shopping_cart) == 0, "Cart should be empty after order"
    
    orders = db.get_orders()
    assert len(orders) == 1, "Should be 1 order in database"
    assert orders[0].get('status') == "Pending", "Order status should be Pending"
    assert orders[0].get('shipping_address') == "Swinburne University, John St, Hawthorn, VIC 3122", "Shipping address should match"
    assert orders[0].get('account_id') == account_id, "Order should be linked to customer account"
    print("place_order() works correctly")
    
    # Test view_order_status
    print("Testing view_order_status()...")
    order_status = customer1.view_order_status(order_id)
    assert order_status.get('order_id') == order_id, "Order ID should match"
    assert order_status.get('status') == "Pending", "Status should be Pending"
    print("view_order_status() works correctly")


def test_team_member_class():
    """Test TeamMember class methods"""
    # Setup
    setup_test_data()
    team_member1 = TeamMember("Riley", "riley@gmail.com")
    
    # Test create_team_member_account
    print("Testing create_team_member_account()...")
    account_id = team_member1.create_team_member_account("riley123", "12345")
    assert account_id == 1, "First account ID should be 1"
    
    accounts = db.get_accounts()
    assert len(accounts) == 1, "Should be 1 account in database"
    assert accounts[0].get('role') == "team_member", "Role should be team_member"
    print("create_team_member_account() works correctly")
    
    # Create a customer and order for testing team member functions
    customer = Customer("tanbeoi", "tanbeoi@gmail.com")
    customer_id = customer.create_account("tanbeoi", "12345")
    customer.add_to_cart(1, 3)
    order_id = customer.place_order("Swinburne University, John St, Hawthorn, VIC 3122")
    
    # Test view_customer_orders
    print("Testing view_customer_orders()...")
    all_orders = team_member1.view_customer_orders()
    assert len(all_orders) == 1, "Should be 1 order in total"
    
    customer_orders = team_member1.view_customer_orders(customer_id)
    assert len(customer_orders) == 1, "Should be 1 order for this customer"
    print("view_customer_orders() works correctly")
    
    # Test update_order_status
    print("Testing update_order_status()...")
    team_member1.update_order_status(order_id, "Shipped")
    orders = db.get_orders()
    assert orders[0].get('status') == "Shipped", "Status should be updated to Shipped"
    print("update_order_status() works correctly")
    
    # Test adjust_stock
    print("Testing adjust_stock()...")
    new_quantity = team_member1.adjust_stock(1, 60)  
    assert new_quantity == 60, "New quantity should be 60"
    
    products = db.get_products()
    assert products[0].get('stock_quantity') == 60, "Stock quantity should be updated"
    print("adjust_stock() works correctly")
    
    # Complete order for sales data testing
    team_member1.update_order_status(order_id, "Completed")
    
    # Test view_sales_data
    print("Testing view_sales_data()...")
    sales_data = team_member1.view_sales_data()
    assert sales_data.get('total_sales') == 30.0, "Total sales should be 30.0"
    assert sales_data.get('order_count') == 1, "Order count should be 1"
    assert sales_data.get('products_sold').get(1) == 3, "3 units of product 1 sold"
    print("view_sales_data() works correctly")

if __name__ == "__main__":
    test_all()