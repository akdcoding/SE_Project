"""
Authors:
    Kyaw Htet Win
    Akshada Thube
    Vruddhi Mehta
    Jency Xavier
"""

from ProductLine import ProductLine
from dataclasses import dataclass

@dataclass
class Item(ProductLine):
    def __init__(self, item_id, warehouse_id, name, sales_price, cost_price):
        super().__init__(name, sales_price, cost_price)
        self.id = item_id
        self.warehouse_id = warehouse_id
        self.dateSold = None
        self.num_available_items += 1

    def __str__(self):
        return "Item ID: " + str(self.item_id) + "\nName: " + self.name + "\nDescription: " + self.description + "\nSales " \
                                                                                                            "Price: " \
                                                                                                            "$" + \
               str(self.sales_price) + "\nCost Price: $" + str(self.cost_price)
               
