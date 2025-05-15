from flask import render_template, request, redirect, url_for
from app.controllers.team_member_controller import TeamMemberController

team_member_controller = TeamMemberController()

def view_orders():
    orders = team_member_controller.get_all_orders()
    return render_template('team_member/view_orders.html', orders=orders)

def update_order_status(order_id):
    if request.method == 'POST':
        new_status = request.form['status']
        team_member_controller.update_order_status(order_id, new_status)
        return redirect(url_for('view_orders'))
    order = team_member_controller.get_order_by_id(order_id)
    return render_template('team_member/update_order_status.html', order=order)

def view_sales_data():
    sales_data = team_member_controller.get_sales_data()
    return render_template('team_member/view_sales_data.html', sales_data=sales_data)