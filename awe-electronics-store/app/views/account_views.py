from flask import render_template, request, redirect, url_for
from app.controllers.account_controller import AccountController

account_controller = AccountController()

def create_account_view():
    if request.method == 'POST':
        account_data = request.form
        account_controller.create_account(account_data)
        return redirect(url_for('account_views.account_success'))
    return render_template('account/create_account.html')

def account_success_view():
    return render_template('account/account_success.html')

def view_account_view(account_id):
    account = account_controller.get_account(account_id)
    return render_template('account/view_account.html', account=account)

def update_account_view(account_id):
    account = account_controller.get_account(account_id)
    if request.method == 'POST':
        updated_data = request.form
        account_controller.update_account(account_id, updated_data)
        return redirect(url_for('account_views.view_account', account_id=account_id))
    return render_template('account/update_account.html', account=account)