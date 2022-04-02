from uuid import uuid4
import pandas as pd
from Item import Item
from utility import *

# Inventory Lookup
class Warehouse:
    def __init__(self):
        self.id = uuid4()
        self.location = ''
        self.capacity = 10
        self.availableItems = []

    def getProductList(self,warehouse_data,items_data):
        data = warehouse_data.split(",")
        self.items = []

        # For each item id in a warehouse_data return item details
        for item_id in data:
            row = items_data.loc[items_data["id"] == int(item_id)]
            if list(row.values) != []:
                self.items.append(Item(int(row.values[0,0]), int(row.values[0,1]), str(row.values[0,2]), float(row.values[0,3]), float(row.values[0,4])))
            
        return self.items

    def updateItemsList(self, newItems=[], warehouseId=1):
        warehouse_data = fetchWarehouseData()
        row = warehouse_data.loc[warehouse_data["id"] == int(warehouseId)]

        # Finding index of row of a warehouse.csv to be updated
        idx = warehouse_data.index[warehouse_data["id"] == int(warehouseId)].tolist()

        # Building a string to update items ids in a warehouse
        res1 = list(map(str, list(row.availableItems)[0].split(",")))
        self.items = res1 + newItems
        delim=","
        res2 = delim.join(self.items)

        warehouse_data.loc[idx[0],'availableItems']=str(res2)

        # Updating warehouse csv
        postWarehouseData(warehouse_data)