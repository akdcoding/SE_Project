from uuid import uuid4
from datetime import date
from Item import Item

"""
    Invoice class handles the entire process of creating a 
    new invoice whenever a customer checks out one or more 
    items at store.
"""


class Invoice:
    def __init__(self, salesman):
        # self.id = uuid4()
        self.id = 10
        self.total = 0.0
        self.subtotal = 0.0
        self.taxAmount = 0.0
        self.shipFees = 0.0
        # Indicates invoice hasn't been settled yet
        self.status = 'Open'
        self.open_date = date.today()
        # Date on which invoice is fully paid
        self.close_date = None
        # Each invoice brought by a particular salesman
        self.salesman = salesman

        self.items = []

    # Passing ids of items customer wants to check out
    def add_items(self, item):
        if isinstance(item, Item):
            self.items.append(item)

    def calculate_sales(self):
        if self.items:
            for item in self.items:
                self.subtotal = self.subtotal + item.sales_price

    def add_tax(self, tax_percent):
        if 0.0 <= tax_percent <= 1.0:
            self.taxAmount = self.subtotal * tax_percent
            self.subtotal = self.subtotal + self.taxAmount

    def add_shipping_fees(self, fees):
        if isinstance(fees, float) and fees >= 0.0:
            self.shipFees = fees
            self.total = self.subtotal + self.shipFees

    def get_invoice_status(self):
        return self.status

    # Called when the full amount of invoice is settled
    def modify_invoice_status(self):
        self.status = 'Close'
        self.close_date = date.today()
