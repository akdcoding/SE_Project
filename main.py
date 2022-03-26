import pandas as pd
from Item import Item
from Invoice import Invoice


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


def main():
    # Unique item id that customer checks out from store
    checkoutitems_id = [1, 2, 5]

    items_data = pd.read_csv("item.csv")

    invoice = Invoice()
    for cid in checkoutitems_id:
        # Retrieves info on item customer wants to check out
        row = items_data.loc[items_data["id"] == cid]
        invoice.add_items(Item(int(row.id), str(row.name), float(row.salesPrice), float(row.costPrice)))

    invoice.calculate_sales()
    invoice.add_tax(0.67)
    invoice.add_shipping_fees(50.00)
    printInvoice(invoice)
    print(','.join([str(i) for i in checkoutitems_id]))
    # id,total,status,openDate,closeDate,items
    # Write this to the invoice.csv database
    newInvoice = {"id": [invoice.id], "total": [invoice.total],
                  "openDate": [invoice.open_date], "closeDate": [invoice.close_date],
                  "items": [','.join([str(i) for i in checkoutitems_id])]}

    invoiceDf = pd.DataFrame(newInvoice)

    # Status of the invoice needs to be updated
    invoiceDf.to_csv("invoice.csv", mode="a", index=False, header=False)

    # Reflected invoice.csv (Database updated)

if __name__ == "__main__":
    main()
