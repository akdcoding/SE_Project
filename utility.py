"""
Authors:
    Kyaw Htet Win
    Akshada Thube
    Vruddhi Mehta
    Jency Xavier
"""

from datetime import date
import pandas as pd
from tabulate import tabulate
from Item import Item


def print_invoice(invoice):
    print("=" * 20 + '\033[1m' + "INVOICE" + '\033[1m' + "=" * 20)
    print("Date: ", invoice.open_date)
    print("Salesman: ", invoice.salesman)
    print("Customer: ", invoice.customer)
    print("-" * 50)
    i = 1

    for item in invoice.items_id:
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


""" Database function """


def update_warehouse_availableItems(newItems=[], warehouseId=1):
    warehouse_data = fetch_warehouse_data()
    row = warehouse_data.loc[warehouse_data["id"] == int(warehouseId)]

    # Finding index of row of a warehouse.csv to be updated
    idx = warehouse_data.index[warehouse_data["id"] == int(warehouseId)].tolist()

    # Building a string to update items_id ids in a warehouse
    res1 = list(map(str, list(row.availableItems)[0].split(",")))
    availableItems = res1 + newItems
    delim = ","
    res2 = delim.join(availableItems)

    warehouse_data.loc[idx[0], 'availableItems'] = str(res2)
    # Database (-)
    # Updating warehouse csv
    post_warehouse_data(warehouse_data)


""" Converts items'id stored in warehouse.csv to Item objects """


def get_item_objects(warehouse_data, items_data):
    items = []
    data = warehouse_data.split(",")
    # For each item_id id in a warehouse_data return item_id details
    for item_id in data:
        row = items_data.loc[items_data["id"] == int(item_id)]
        if list(row.values):
            items.append(
                Item(int(row.values[0, 0]), int(row.values[0, 1]), str(row.values[0, 2]), float(row.values[0, 3]),
                     float(row.values[0, 4])))

    return items


"""Adds a newly created item_id to item_id.csv & warehouse.csv"""


def update_item_warehouse(Item, warehouse):
    newItem = {"id": [Item.id], "warehouseid": [warehouse.id], "name": [Item.name],
               "salesprice": [Item.sales_price], "costprice": [Item.cost_price],
               "datesold": [Item.dateSold]}
    itemDf = pd.DataFrame(newItem)
    # Add new item_id to csv
    post_item_data(itemDf)


def fetch_inventory():
    items_data = pd.read_csv("item.csv")
    return items_data


def fetch_warehouse_data():
    warehouse_data = pd.read_csv("warehouse.csv", header=0)
    return warehouse_data


def post_warehouse_data(warehouse_data):
    warehouse_data.to_csv("warehouse.csv", index=False, header=True)


def post_item_data(item_data):
    item_data.to_csv("item_id.csv", index=False, header=False, mode="a", )
