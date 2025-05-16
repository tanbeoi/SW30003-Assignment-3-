import json
from pathlib import Path

current_working_dir = Path.cwd()
print(current_working_dir)

data_path = current_working_dir / "awe-electronics-store" / "json_test" / "test.json"


print(data_path)
class dataBase():
    def __init__(self, json_file):
        self.json_file = json_file

    def add_user_account(self,username, password, email):
        new_user = {
            "username": username,
            "password": password,
            "email": email
        }

        # read existing data
        with open(self.json_file, 'r') as file:
            users = json.load(file)
        # Add new user
        users.append(new_user)
        # Write to the file
        with open(self.json_file, 'w') as file:
            json.dump(users, file, indent=4)

# testing
db = dataBase(data_path)
db.add_user_account('test_user', 'test_password', 'test_email@test_email')