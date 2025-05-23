
import json
from pathlib import Path

# generic database class. This can be inherited from 
class dataBase():
    # for the database this is a generic template
    def __init__(self, json_file):
        current_working_dir = Path.cwd()
        self.json_file = current_working_dir / "awe-electronics-store" / "database" / json_file

    def delete_by_id(self, id_name, id_number):
        # Load the existing json data file
        with open(self.json_file, 'r') as file:
            data = json.load(file)
        # find the data point which does not match
        new_data =[] 
        for dic in data:
            if dic.get(id_name) != id_number:
                new_data.append(dic)
        #rewrite the json file without the old id in it
        with open(self.json_file, 'w') as file:
            json.dump(new_data, file, indent=4)


    def retrive_by_id(self, id_name, id_number):
        # Load the existing json data file
        with open(self.json_file, 'r') as file:
            data = json.load(file)
        # find the data point which does not match
        for dic in data:
            if dic.get(id_name) == id_number:
                return dic
        #else
        return None

    def get_next_id(self, id_name):
        with open(self.json_file, 'r') as file:
            data = json.load(file)
        if not data:
            return 1
        return max(item[id_name] for item in data) + 1
    

    def get_all(self):
        with open(self.json_file, 'r') as file:
            data = json.load(file)
        return data

 
# inherits dataBase class
class productDatabase(dataBase):
    def __init__(self, json_file):
        super().__init__(json_file)

    def add_product(self,name, description, price, stock_quantity):
        new_product = {
            "product_id": self.get_next_id("product_id"),
            "name": name,
            "description": description,
            "price": price,
            "stock_quantity": stock_quantity
        }
        # read existing data
        with open(self.json_file, 'r') as file:
            data = json.load(file)
        # Add new
        data.append(new_product)
        # Write to the file
        with open(self.json_file, 'w') as file:
            json.dump(data, file, indent=4)

        # not all database things should be updateable but this is a generic implamentation
    def update_product_by_id(self, product_id, chosen_entry, new_value):
        with open(self.json_file, 'r') as file:
            data = json.load(file)

        # if item is found
        found = False
        # find by ID loop through each dic in file
        for dic in data:
            if dic.get("product_id") == product_id:
                # Update data once found and exit loop
                dic[chosen_entry] = new_value  
                found = True
                break

        # Write the updated data to file
        if found:
            with open(self.json_file, 'w') as file:
                json.dump(data, file, indent=4)
            # boolean for confirmation of update
            return True
        else:
            return False  


#########################################################################################################################
#testing all code

test_product_db = productDatabase("Product.json")

all_data = test_product_db.get_all()
print("Testing list all products")
# view list of data
for i in all_data:
    print(i)

#create a new product
test_product_db.add_product(name="Mouse Pad", description="Very warm", price=50, stock_quantity=5)
print("Testing list all product with new addition")
#check if it has been added
for i in all_data:
    print(i)

#update product description of newly created Mouse Pad
test_product_db.update_product_by_id(product_id=3, chosen_entry="description", new_value="Very warm and clean!")
print("Testing updating of new product and retrieve single item")
# test get by id for the updated product
print(test_product_db.retrive_by_id(id_name="product_id", id_number=3))

print("Testing product deletion")

test_product_db.delete_by_id(id_name="product_id", id_number=3)

#check if it has been deleted
for i in all_data:
    print(i)
