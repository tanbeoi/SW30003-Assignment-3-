from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    from app.views import account_views, product_views, order_views
    
    app.register_blueprint(account_views.bp)
    app.register_blueprint(product_views.bp)
    app.register_blueprint(order_views.bp)
    
    # Add a home route
    from flask import render_template
    
    @app.route('/')
    def home():
        return render_template('base.html')
        
    return app

