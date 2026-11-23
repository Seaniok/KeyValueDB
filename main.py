import json


class KeyValueDB:
    def __init__(self, filename):
        self.filename = filename
        self.storage = {}
        
        try:
            with open(filename, 'w') as db_file:
                db_file.close()
        except FileExistsError(filename):
            pass        

    def __set__(self, instance, value):
        self.storage[instance] = value

    def __getitem__(self, key):
        try:
            print(self.storage[key])
        except KeyError:
            print(f"There is no key named {key} !")

    def save_data_on_file(self):
        try:
            with open(self.filename, 'a') as db_file:
                if self.storage:
                    db_file.write(json.dumps(self.storage))
        except FileNotFoundError:
            print("File Not Found - bug")


        