from unittest import TestCase
from Item import Item
from Invoice import Invoice
from datetime import date


class InvoiceTestCases(TestCase):

    def setUp(self):
        self.item1 = Item(5, "iFloss", 30.10, 20.20, 10.00)
        self.item2 = Item(4, "Drone", 45.00, 10.00, 4.500)
        self.invoice = Invoice("MR. WIN", "MRs.WIN")

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

        tax = 0.2 * self.invoice.subtotal
        self.invoice.add_tax(0.2)
        self.assertEqual(tax, self.invoice.taxAmount)

    def test_add_shipping_fees(self):
        
        self.invoice.add_shipping_fees(-1000.00)
        self.assertEqual(0.0, self.invoice.shipFees)
        
        self.invoice.add_shipping_fees("hello")
        self.assertEqual(0.0, self.invoice.shipFees)

        self.invoice.add_shipping_fees(100.00)
        self.assertEqual(100, self.invoice.shipFees)
        self.assertEqual(100, self.invoice.total)

    def test_modify_invoice_status(self):

        self.invoice.modify_invoice_status()
        today = date.today()
        self.assertEqual(today, self.invoice.close_date)
        self.assertEqual("Close", self.invoice.status)
