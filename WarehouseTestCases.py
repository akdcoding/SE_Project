from unittest import TestCase
from Warehouse import Warehouse


class WarehouseTestCases(TestCase):

    def setUp(self):
        self.warehouse = Warehouse()

    def test_set_availableItems(self):
        # Bad values of item_id id are passed
        self.warehouse.set_availableItems("abcdefg")
        self.assertEqual(self.warehouse.availableItemsId, [])
        
        self.warehouse.set_availableItems([])
        self.assertEqual(self.warehouse.availableItemsId, [])
        
        # Good values
        productIds = ["1", "2", "3"]
        self.warehouse.set_availableItems(productIds)
        self.assertEqual(self.warehouse.availableItemsId, productIds)

    def test_update_item_list(self):
        self.warehouse.update_item_list([-400])
        self.assertEqual(self.warehouse.availableItemsId, [])

        self.warehouse.update_item_list(["100"])
        self.assertEqual(self.warehouse.availableItemsId, ["100"])