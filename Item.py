from ProductLine import ProductLine


class Item(ProductLine):
    def __init__(self, id, name, sales_price, cost_price):
        super().__init__(name, sales_price, cost_price)
        self.id = id
        self.dateSold = ''
        self.num_available_items += 1

    def __str__(self):
        return "id: " + str(self.id) + " name: " + self.name + " Sales Price: $" + str(
            self.sales_price) + " Cost Price: $" + str(self.cost_price)
