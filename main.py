import pandas as pd
from Item import Item
from Invoice import Invoice
from utility import print_invoice

CUSTOMER_TAXPERCENT = 0.095
SHIPPING_FEES = 4.99


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


if __name__ == "__main__":
    main()
