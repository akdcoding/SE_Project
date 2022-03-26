# Product_Line
class ProductLine:
    def __init__(self, name, sales_price, cost_price):

        self.name = name
        self.sales_price = sales_price
        self.cost_price = cost_price
        self.total_items_sold = 0
        self.num_available_items = 0

    def getProductDetails(self):
        return self.name, self.sales_price, self.cost_price, self.total_items_sold

"""
    iPhone 13:
    - Models: iPhone 13 or iPhone 13x
    
    SKU: Number Barcode Scanner
    Invoice:
     - iPhone 13     
"""