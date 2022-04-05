from uuid import uuid4


# Inventory Lookup
class Warehouse:
    def __init__(self):
        self.id = uuid4()
        self.location = ''
        self.capacity = 10
        # Must be a list of integer ids in string format(Items in warehouse)
        self.availableItemsId = []

    def set_availableItems(self, items):
        if items:
            try:
                if any(isinstance(item, str) for item in items) and any(isinstance(int(item), int) for item in items):
                    self.availableItemsId = items
            except ValueError:
                print("Item id must be valid integer")

    def update_item_list(self, newItemIds):
        # Update availableItemsId with a new single item_id id
        if newItemIds:
            try:
                if any(isinstance(item, str) for item in newItemIds) and any(isinstance(int(item), int) for item in newItemIds):
                    self.availableItemsId += newItemIds
            except ValueError:
                print("New items_id ID must be integer")
