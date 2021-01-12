from pizzapy import Customer, StoreLocator, Order, CreditCard

customer = Customer("first name", "last name", "email", "phone number", "address")

my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
print(my_local_dominos)

menu = my_local_dominos.get_menu()

order = Order.begin_customer_order(customer, my_local_dominos, "ca")
order.add_item("14SCPFEAST")
order.add_item("2LCOKE")


print("\n" + str(order))

total = 0
for item in order.data["Products"]:
    price = item["Price"]
    print(item["Name"]+" $ " + price)
    total += float(price)
print ("\n Order total is $" + str(total) + " (tax and delivery fees excluded)")

#card = CreditCard("number", "expiry", "cvv", "posdtal code")

#order.place(card)
#my_local_dominos.place_order(order, card)
