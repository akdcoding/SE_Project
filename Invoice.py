from uuid import uuid4
from datetime import date

"""
    Invoice class handles the entire process of creating a 
    new invoice whenever a customer checks out a one or more 
    items at store.
"""

class Invoice:
    def __init__(self):
        self.id = uuid4()
        self.total = 0.0
        self.subtotal = 0.0
        self.taxAmount = 0.0
        self.shipFees = 0.0
        self.status = 'Open'
        self.open_date = date.today()
        self.close_date = ''
        self.items = []

    # Passing ids of items customer wants to check out
    def add_items(self, item):
        self.items.append(item)

    def calculate_sales(self):
        for item in self.items:
            self.subtotal = self.subtotal + item.sales_price

    def add_tax(self, taxPercent):
        self.taxAmount = self.subtotal * taxPercent
        self.subtotal = self.subtotal + self.taxAmount

    def add_shipping_fees(self, fees):
        self.shipFees = fees
        self.total = self.subtotal + self.shipFees

    def get_invoice_status(self):
        return self.status

    def modify_invoice_status(self):
        self.status = 'Close'
        self.close_date = date.today()
