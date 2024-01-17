import json
from BStore_Item import Item
import pandas as pd

class DvdDb(Item):
    def __init__(self, init=False, db="dvdstore.csv"):
        self.database = dict()
        self.file = db
        self.fileJSON = 'dvdstoreJSON.json'

    def display_data(self):
        tuplelist = list()
        for i in self.database:
            tuplelist.append(self.database[i])
        print("DB Displayed")
        return tuplelist
    
    def add_item(self, num, name, year, genre, price, availb): 
        base = Item(num, name, year, genre, price, availb)
        update = base.tuple
        self.database[num] = update
        print("DB Added Item")

    def update_item(self, num, name, year, genre, price, availb): 
        DvdDb.update_item(self, num, name, year, genre, price, availb)

    def deleteItem(self, num):
        del self.database[num]

    def importcsv(self):
        data = pd.read_csv(f"{self.file}") 
        lst = data.values.tolist()

        for num in range(len(lst[0])):
            listing = self.database[lst[num][num]] = list()
            for entry in range(len(lst)):
                listing.append(lst[entry][num])

    def exportcsv(self):
        set = pd.DataFrame(self.database)
        set.to_csv(f"{self.file}", index=False)

    def num_check(self,id):
        if self.database.get(id) is not None:
            return True
        else:
            return False
        
    def extract_to_json(self):
        data = self.database
        with open(self.fileJSON, 'w') as f:
            json.dump(data, f)