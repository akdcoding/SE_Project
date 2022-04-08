"""
Authors:
    Kyaw Htet Win
    Akshada Thube
    Vruddhi Mehta
    Jency Xavier
"""
from Item import Item


class Warehouse:
    def __init__(self, id):
        self.id = id
        self.location = ''
        self.capacity = 10
        # Available items in warehouse (Inventory lookup)
        self.availableItems = []

    def set_availableItems(self, items):
        if items:
            # Must be a list of valid Item objects
            if any(isinstance(item, Item) for item in items):
                self.availableItems = items

    def update_item_list(self, newItem):
        if isinstance(newItem, Item):
            self.availableItems.append(newItem)
