from django.shortcuts import render, redirect
from app.controllers.product_controller import productDatabase

product_db = productDatabase("Product.json")

def add_new_product_view(request):
    if request.method == "POST":
        # get data from submit form
        name = request.POST.get("name")
        description = request.POST.get("description")
        # cannot be bothered with floats
        price = int(request.POST.get("price"))
        stock_quantity = int(request.POST.get("stock_quantity"))
        # use the instance of the database to add it
        product_db.add_product(name, description, price, stock_quantity)
        # if successful return to product management
        return render(request, "product_management.html")
    #otherwise return to product management again
    return render(request, "product_management.html")

def update_product_view(request):
    if request.method == "POST":
        # get values from form
        # dropdown box with item name included
        product_id = int(request.POST.get("product_id"))
        # drop down box
        chosen_entry = request.POST.get("field")
        #text_box
        new_value = request.POST.get("value")
        # update
        product_db.update_product_by_id(product_id,chosen_entry, new_value)
        return render(request, "product_management.html")
    #otherwise return to product management again
    return render(request, "product_management.html")

def delete_product_view(request):
    if request.method == "POST":
        # delete functionality is covered in parent 
        id_name= "product_id"
        id_number = int(request.POST.get("product_id"))

        product_db.delete_by_id(id_name, id_number)
        return render(request, "product_management.html")
    #otherwise return to product management again
    return render(request, "product_management.html")

# to get list of all stock items. 
# this will be helpful for populating form information
def product_list_view(request):
    stock = product_db.get_all()
    return render(request, "product_management.html", {"products": stock})