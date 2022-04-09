"""
Authors:
    Kyaw Htet Win
    Akshada Thube
    Vruddhi Mehta
    Jency Xavier
"""

from unittest import TestCase, TextTestRunner
from Item import Item
from Invoice import Invoice
from datetime import date
import logging
import sys


class InvoiceTestCases(TestCase):

    def setUp(self):
        # Create sample items to checkout
        CUSTOMER = "Mrs.Win"
        SALES_MAN = "Mr. Win"
        self.item1 = Item(5, 2, "iFloss", 30.10, 20.20)
        self.item2 = Item(4, 1, "Drone", 45.00, 10.00)
        self.invoice = Invoice(CUSTOMER, SALES_MAN)

    def test_add_items(self):
        # Entering something other than Item object
        self.invoice.add_items("Whatever")
        self.assertEqual([], self.invoice.items_id)

        self.invoice.add_items(self.item1)
        self.assertEqual(self.item1, self.invoice.items_id[0])

    def test_calculate_sales(self):
        # Sales shouldn't be calculated without any items_id to check out
        self.invoice.calculate_sales()
        self.assertEqual(0.0, self.invoice.subtotal)

        # Subtotal for two items_id
        subtotal = self.item1.sales_price + self.item2.sales_price
        self.invoice.add_items(self.item1)
        self.invoice.add_items(self.item2)
        self.invoice.calculate_sales()
        self.assertEqual(subtotal, self.invoice.subtotal)

    def test_add_tax(self):
        self.invoice.add_items(self.item1)
        self.invoice.calculate_sales()

        # Shouldn't calculate tax with invalid tax percentage entered
        self.invoice.add_tax(450)
        self.assertEqual(0.0, self.invoice.taxAmount)

        CUSTOMER_TAXPERCENT = 0.095
        tax = CUSTOMER_TAXPERCENT * self.invoice.subtotal
        self.invoice.add_tax(CUSTOMER_TAXPERCENT)
        self.assertEqual(tax, self.invoice.taxAmount)

    def test_add_shipping_fees(self):
        
        self.invoice.add_shipping_fees(-1000.00)
        self.assertEqual(0.0, self.invoice.shipFees)
        
        self.invoice.add_shipping_fees("hello")
        self.assertEqual(0.0, self.invoice.shipFees)

        SHIPPING_FEES = 4.99
        self.invoice.add_shipping_fees(SHIPPING_FEES)
        self.assertEqual(SHIPPING_FEES, self.invoice.shipFees)
        self.assertEqual(SHIPPING_FEES, self.invoice.total) # No items added here

    def test_modify_invoice_status(self):

        self.invoice.modify_invoice_status()
        today = date.today()
        self.assertEqual(today, self.invoice.close_date)
        self.assertEqual("Close", self.invoice.status)


