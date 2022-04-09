"""
Authors:
    Kyaw Htet Win
    Akshada Thube
    Vruddhi Mehta
    Jency Xavier
"""

from unittest import TestCase
from Item import Item
from Warehouse import Warehouse
from utility import *


class WarehouseTestCases(TestCase):

    def setUp(self):
        self.warehouse = Warehouse(id=1)

    def test_set_availableItems(self):
        # Bad values of item_id id are passed
        self.warehouse.set_availableItems("abcdefg")
        self.assertEqual(self.warehouse.availableItems, [])

        self.warehouse.set_availableItems([])
        self.assertEqual(self.warehouse.availableItems, [])

        # Good values
        items = [Item(8, 1, 'Logitech S150 USB Speakers with Digital Sound', 500.00, 350.50),
                 Item(5, 1, "iFloss", 30.10, 20.20)]
        self.warehouse.set_availableItems(items)
        self.assertEqual(self.warehouse.availableItems, items)

    def test_update_item_list(self):
        # Passing inappropriate item to update the warehouse available items
        self.warehouse.update_item_list([-400])
        self.assertEqual(self.warehouse.availableItems, [])

        newItem = Item(8, 2, 'Logitech S150 USB Speakers with Digital Sound', 500.00, 350.50)
        self.warehouse.update_item_list(newItem)
        self.assertEqual(self.warehouse.availableItems, [newItem])

    def test_inventory_lookup(self):
        """
        Demonstrates test for inventory lookup process 
        """
        # Load warehouse database & retrieve info on the current warehouse
        warehouse_data = fetch_warehouse_data()
        items_id = str(warehouse_data.loc[self.warehouse.id - 1, "availableItems"])

        # Load items.csv database for Item details
        items_data = fetch_inventory()
        items = get_item_objects(warehouse_data=items_id, items_data=items_data)

        self.warehouse.set_availableItems(items)
        self.assertEqual(self.warehouse.availableItems, items)

        # Now warehouse's availableItems contain all items to display for user (UI component)
