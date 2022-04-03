from datetime import date
import pandas as pd
from tabulate import tabulate


def print_invoice(invoice):
    print("=" * 20 + '\033[1m' + "INVOICE" + '\033[1m' + "=" * 20)
    print("Date: ", invoice.open_date)
    print("Salesman: ", invoice.salesman)
    print("-" * 50)
    i = 1

    for item in invoice.items:
        name = item.name
        price = ("$" + str(item.sales_price)).ljust(25)
        print(f"[{i}]", name + "     " + price)
        i += 1

    print("\nTAX: $", invoice.taxAmount)
    print("Subtotal: $", invoice.subtotal)
    print("Shipping Fees: $", invoice.shipFees)
    print("Total: $", invoice.total)


def print_inventory(warehouseIds, warehouse_inventory):
    print("\n\n\n" + "=" * 20 + '\033[1m' + "INVENTORY" + '\033[1m' + "=" * 20)
    print("Date: ", date.today())
    print("-" * 50 + '\n')
    i = 1
    counter = 0

    for warehouseData in warehouse_inventory:
        print('\nWarehouse ' + str(warehouseIds[counter]))
        print("-" * 50 + '\n')
        warehouse_data_arr = []
        for inventoryItem in warehouseData:
            item_arr = [inventoryItem.id, inventoryItem.name, inventoryItem.sales_price, inventoryItem.cost_price]
            i += 1
            warehouse_data_arr.append(item_arr)
        counter += 1
        print(tabulate(warehouse_data_arr, headers=["Id", "Name", "Price", "Cost"]))


def fetch_inventory():
    items_data = pd.read_csv("item.csv")
    return items_data


def fetch_warehouse_data():
    warehouse_data = pd.read_csv("warehouse.csv", header=0)
    return warehouse_data


def post_warehouse_data(warehouse_data):
    warehouse_data.to_csv("warehouse.csv", index=False, header=True)


def post_item_data(item_data):
    item_data.to_csv("item.csv", index=False, header=False, mode="a", )
