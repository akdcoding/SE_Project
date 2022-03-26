from uuid import uuid4
# Inventory Lookup
class Warehouse:
    def __init__(self, id, location, capacity, items):
        self.id = uuid4()
        self.location = location
        self.capacity = capacity
        self.items = items

    def getProductList(self):
        return (self.id, self.location, self.capacity, self.items)

    def updateItemsList(self, items):
        self.items.append(items)