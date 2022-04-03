from ProductLine import ProductLine
import pandas as pd
from utility import *


class Item(ProductLine):
    def __init__(self, id, warehouse_id, name, sales_price, cost_price):
        super().__init__(name, sales_price, cost_price)
        self.id = id
        self.warehouseid = warehouse_id
        self.name=name
        self.dateSold = None
        self.sales_price = sales_price
        self.cost_price = cost_price
        self.num_available_items += 1

    def __str__(self):
        return "Item ID: " + str(self.id) + "\nName: " + self.name + "\nDescription: " + self.description + "\nSales " \
                                                                                                            "Price: " \
                                                                                                            "$" + \
               str(self.sales_price) + "\nCost Price: $" + str(self.cost_price)
               
    def addItem(self,warehouse):
        newItem = {"id": [self.id], "warehouseid":[self.warehouseid], "name": [self.name],
                "salesprice": [self.sales_price], "costprice": [self.cost_price],
                "datesold": [self.dateSold]}
        itemDf = pd.DataFrame(newItem)
        warehouse.update_item_list([str(self.id)], self.warehouseid)

        # Add new item to csv
        post_item_data(itemDf)