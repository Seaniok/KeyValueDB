import json


class KeyValueDB:
    def __init__(self, filename):
        self.filename = filename

        try:
            with open(filename) as db_file:
                self.storage = json.load(db_file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.storage = {}

    def __setitem__(self, key, value):
        if key in self.storage:
            self.storage[key] = list(self.storage[key])
            self.storage[key].append(value)
            self.save_data_on_file()
        else:
            self.storage[key] = value
            self.save_data_on_file()

    def __getitem__(self, key):
        return self.storage[key]

    def save_data_on_file(self):
        with open(self.filename, 'w') as db_file:
                json.dump(self.storage, db_file, indent=4)
