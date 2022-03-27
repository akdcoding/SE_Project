

def print_invoice(invoice):
    print("="*20 + '\033[1m' + "INVOICE" + '\033[1m' + "="*20)
    print("Date: ", invoice.open_date)
    print("-"*50)
    i = 1

    for item in invoice.items:
        name = item.name
        price = ("$"+str(item.sales_price)).rjust(25)
        print(f"[{i}]", name + price)
        i += 1

    print("\nTAX: $", invoice.taxAmount)
    print("Subtotal: $", invoice.subtotal)
    print("Shipping Fees: $", invoice.shipFees)
    print("Total: $", invoice.total)
