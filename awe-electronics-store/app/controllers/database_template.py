from pathlib import Path
import json
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

