
import json
from pathlib import Path


# generic database class. This can be inherited from 
class dataBase():
    def __init__(self, json_file):
        current_working_dir = Path.cwd()
        self.json_file = current_working_dir / "awe-electronics-store" / "database" / json_file

    def add_new():
        pass

    def delete_by_id():
        pass

    def retrive_by_id():
        pass

    def get_next_id(self):
        try:
            with open(self.json_file, 'r') as file:
                data = json.load(file)
            if not data:
                return 1
            return max(item["id"] for item in data) + 1
        except FileNotFoundError:
            return 1
        except json.JSONDecodeError:
            return 1


    
        

    
# inherits dataBase class
class productDb(dataBase):
    def __init__(self, json_file):
        super().__init__(json_file)

    def add_product(self,name, description, price, stock_quantity):
        new_product = {
            "id": self.get_next_id(),
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
            json.dump(new_product, file, indent=4)


    def update_product(self, product_id, updated_data):
        # Logic to update an existing product in the database
        pass

