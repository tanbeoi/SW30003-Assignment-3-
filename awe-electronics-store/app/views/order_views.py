from flask import render_template, request, redirect, url_for
from app.controllers.order_controller import OrderController

order_controller = OrderController()

def place_order_view():
    if request.method == 'POST':
        order_data = request.form
        order_controller.place_order(order_data)
        return redirect(url_for('order_success_view'))
    return render_template('orders/place_order.html')

def order_success_view():
    return render_template('orders/order_success.html')

def view_order_view(order_id):
    order = order_controller.get_order(order_id)
    return render_template('orders/view_order.html', order=order)

def update_order_status_view(order_id):
    if request.method == 'POST':
        new_status = request.form['status']
        order_controller.update_order_status(order_id, new_status)
        return redirect(url_for('view_order_view', order_id=order_id))
    order = order_controller.get_order(order_id)
    return render_template('orders/update_order_status.html', order=order)