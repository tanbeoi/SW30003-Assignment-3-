# Configuration settings for the AWE Electronics Store application

import os

class Config:
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'json:///data/accounts.json'
    ORDERS_URI = 'json:///data/orders.json'
    PRODUCTS_URI = 'json:///data/products.json'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')
    JSONIFY_PRETTYPRINT_REGULAR = True

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'json:///data/test_accounts.json'
    ORDERS_URI = 'json:///data/test_orders.json'
    PRODUCTS_URI = 'json:///data/test_products.json'