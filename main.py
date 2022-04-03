from numpy import number
import pandas as pd
from Item import Item
from Invoice import Invoice
from utility import *
from Warehouse import Warehouse

CUSTOMER_TAXPERCENT = 0.095
SHIPPING_FEES = 4.99
SALES_MAN = "Mr. Win"

def main():

    # Ids of items that customer checks out from store
    checkedout_items_id = [1, 2, 5, 2]

    invoice = Invoice(salesman=SALES_MAN)

    # Database retrieval
    items_data = fetch_inventory()
    for cid in checkedout_items_id:
        # Retrieves info on item customer wants to check out
        row = items_data.loc[items_data["id"] == cid]
        warehouse_id = int(row.values[0,1])
        name = row.values[0, 2]
        sales_price = float(row.values[0, 3])
        cost_price = float(row.values[0, 4])
        invoice.add_items(Item(cid, warehouse_id, name, sales_price, cost_price))
    invoice.calculate_sales()
    invoice.add_tax(CUSTOMER_TAXPERCENT)
    invoice.add_shipping_fees(SHIPPING_FEES)
    print_invoice(invoice)

    # TODO: Write the new invoice data to database("invoice.csv")

    # Inventory Lookup
    warehouse = Warehouse()

    # Adding new item to add new row in item.csv and adding new items to warehouse 2
    newItem = Item(8,2,'Logitech S150 USB Speakers with Digital Sound', 500.00, 350.50)
    newItem.addItem(warehouse)
    
    # print inventory of each warehouse
    warehouse_data = fetch_warehouse_data()
    warehouse_inventory = []
    warehouseIds = []

    for i in range(len(warehouse_data)):
        itemIds = warehouse.get_product_list(str(warehouse_data.loc[i, "availableItems"]), items_data)
        warehouseIds.append(warehouse_data.loc[i, "id"])
        warehouse_inventory.append(itemIds)
    print_inventory(warehouseIds,warehouse_inventory)


    

if __name__ == "__main__":
    main()
