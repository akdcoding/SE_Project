from ProductLine import ProductLine


class Item(ProductLine):
    def __init__(self, id, name, sales_price, cost_price):
        super().__init__(name, sales_price, cost_price)
        self.id = id
        self.dateSold = None
        self.num_available_items += 1

    def __str__(self):
        return "Item ID: " + str(self.id) + "\nName: " + self.name + "\nDescription: " + self.description + "\nSales " \
                                                                                                            "Price: " \
                                                                                                            "$" + \
               str(self.sales_price) + "\nCost Price: $" + str(self.cost_price)
