from uuid import uuid4
import pandas as pd
from Item import Item

# Inventory Lookup
class Warehouse:
    def __init__(self):
        self.id = uuid4()
        self.location = ''
        self.capacity = 10
        self.availableItems = []

    def getProductList(self,warehouse_data):
        items_data = pd.read_csv("item.csv")
        data = warehouse_data.split(",")
        self.items = []

        # For each item id in a warehouse_data return item details
        for item_id in data:
            row = items_data.loc[items_data["id"] == int(item_id)]
            self.items.append(Item(int(row.id), str(row.name), float(row.salesPrice), float(row.costPrice)))
            
        return self.items

    def updateItemsList(self, newItems=[], warehouseId=1):
        items_data = pd.read_csv("warehouse.csv")
        row = items_data.loc[items_data["id"] == int(warehouseId)]

        # Finding index of row of a warehouse.csv to be updated
        idx = items_data.index[items_data["id"] == int(warehouseId)].tolist()

        # Building a string to update items ids in a warehouse
        res1 = list(map(str, list(row.availableItems)[0].split(",")))
        self.items = res1 + newItems
        delim=","
        res2 = delim.join(self.items)

        items_data.loc[idx[0],'availableItems']=str(res2)

        # Updating warehouse csv
        items_data.to_csv("warehouse.csv", index=False, header=True)
