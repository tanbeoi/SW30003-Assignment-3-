from django.shortcuts import render
from controllers.product_controller import productDatabase


product_db = productDatabase("Product.json")

def add_new_product():
    pass

def update_product():
    pass


def get_product_list():
    pass

def update_product():
    pass
# from flask import render_template, request, redirect, url_for
# from app.controllers.product_controller import ProductController

# product_controller = ProductController()

# def list_products():
#     products = product_controller.get_all_products()
#     return render_template('products/list.html', products=products)

# def view_product(product_id):
#     product = product_controller.get_product_by_id(product_id)
#     return render_template('products/view.html', product=product)

# def add_product():
#     if request.method == 'POST':
#         product_data = request.form.to_dict()
#         product_controller.add_product(product_data)
#         return redirect(url_for('list_products'))
#     return render_template('products/add.html')

# def update_product(product_id):
#     product = product_controller.get_product_by_id(product_id)
#     if request.method == 'POST':
#         updated_data = request.form.to_dict()
#         product_controller.update_product(product_id, updated_data)
#         return redirect(url_for('view_product', product_id=product_id))
#     return render_template('products/update.html', product=product)

# def delete_product(product_id):
#     product_controller.delete_product(product_id)
#     return redirect(url_for('list_products'))