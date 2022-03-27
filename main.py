from numpy import number
import pandas as pd
from Item import Item
from Invoice import Invoice
from utility import print_invoice

CUSTOMER_TAXPERCENT = 0.095
SHIPPING_FEES = 4.99
from Warehouse import Warehouse

def printInvoice(invoice):
    print("INVOICE")
    print("Date: ", invoice.open_date)
    for item in invoice.items:
        itemName = item.name
        salesPrice = item.sales_price
        print(f"{itemName} ${salesPrice}")

    print("\nTAX: $", invoice.taxAmount)
    print("\nSubtotal: $", invoice.subtotal)

    print("\nShipping Fees: $", invoice.shipFees)
    print("\nTotal: $", invoice.total)

def printInventory(warehouseIds, warehouse_inventory):
    counter = 0
    for warehouseData in warehouse_inventory:
        print('\nWarehouse '+ str(warehouseIds[counter]))
        for inventoryItem in warehouseData:
            itemName = inventoryItem.name
            salesPrice = inventoryItem.sales_price
            print(f"{itemName} ${salesPrice}")
        counter +=1



def main():

    # Ids of items that customer checks out from store
    checkedout_items_id = [1, 2, 5, 2]

    invoice = Invoice()

    # Database retrieval
    items_data = pd.read_csv("item.csv")
    for cid in checkedout_items_id:
        # Retrieves info on item customer wants to check out
        row = items_data.loc[items_data["id"] == cid]
        name = row.values[0, 1]
        sales_price = float(row.values[0, 2])
        cost_price = float(row.values[0, 3])
        invoice.add_items(Item(cid, name, sales_price, cost_price))

    invoice.calculate_sales()
    invoice.add_tax(CUSTOMER_TAXPERCENT)
    invoice.add_shipping_fees(SHIPPING_FEES)
    print_invoice(invoice)

    # TODO: Write the new invoice data to database("invoice.csv")


    # Inventory Lookup
    warehouse = Warehouse()
    warehouse_data = pd.read_csv("warehouse.csv", header=0)
    warehouse_inventory = []
    warehouseIds = []
    
    #print(warehouse_data)
    for i in range(len(warehouse_data)):
        itemIds = warehouse.getProductList(str(warehouse_data.loc[i, "availableItems"]))
        warehouseIds.append(warehouse_data.loc[i, "id"])
        
        warehouse_inventory.append(itemIds)
    printInventory(warehouseIds,warehouse_inventory)
    warehouse.updateItemsList(['6','7'],2)

    

if __name__ == "__main__":
    main()
