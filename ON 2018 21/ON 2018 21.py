items = ["French fries", "1/4 pound burger", "1/4 pound cheeseburger","1/2 pound burger","1/2 pound cheeseburger","Medium pizza","Medium pizza with extra toppings","Medium pizza","Large pizza with extra toppings","Garlic bread"]
price = [2,5,5.55,7,7.5,9,11,12,14.5,4.5]
code = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]
order_sub_item = []
order_sub_quantity = []
order_sub_price = []
total_price = []
unique_id = []

uorder_code = 99


def a():

    request = input("do you want to give order? ")
    print("")
    print("")
    if request == "y":
        global uorder_code
        uorder_code = uorder_code + 1
        mkzero()
        order_request()

    elif request == "n":
        margin = int(input("Input profit percentage"))
        takings = int(sum(total_price))
        profit = (takings/100) * margin

        print("today taking were", takings)
        print("% profit is ", margin)
        print("profit is", profit)
        input()
        exit()

    else:
        print("Input not valid")
        a()

def mkzero():

    del order_sub_item[:]
    del order_sub_quantity[:]
    del order_sub_price[:]

def order_request():

    def order():

        order_code = input("Enter order code - ")
        order_item = items[code.index(order_code)]
        order_sub_item.append(order_item)
        order_quantity = int(input("Enter order quantity - "))
        order_sub_quantity.append(order_quantity)

        order_price = int(price[code.index(order_code)] * order_quantity)
        order_sub_price.append(order_price)

        order_flow()

    def order_flow():
        print("")

        flow = input("do you want to eat more?")
        if flow == "y":
            print("")
            order()

        elif flow == "n":
            print("")
            print("")
            order_total_price = int(sum(order_sub_price))
            total_price.append(order_total_price)
            unique_id.append(uorder_code)

            print("items = ", order_sub_item)
            print("quantities",order_sub_quantity)
            print("prices",order_sub_price)
            print("totalprice = ", total_price[uorder_code - 100])
            print("unique ID =", uorder_code)
            print("")
            print("")
            a()

        else:
            print("Input not valid")
            order()


    order()
    order_flow()

def menu():
    print("                 Menu")
    print("")
    print("Item Code        Items                                        Price")
    print("  ", code[0], "       ", items[0], "                                   ", price[0], "$")
    print("  ", code[1], "       ", items[1], "                               ", price[1], "$")
    print("  ", code[2], "       ", items[2], "                         ", price[2], "$")
    print("  ", code[3], "       ", items[3], "                               ", price[3], "$")
    print("  ", code[4], "       ", items[4], "                         ", price[4], "$")
    print("  ", code[5], "       ", items[5], "                                   ", price[5], "$")
    print("  ", code[6], "       ", items[6], "               ", price[6], "$")
    print("  ", code[7], "       ", items[7], "                                   ", price[7], "$")
    print("  ", code[8], "       ", items[8], "                ", price[8], "$")
    print("  ", code[9], "       ", items[9], "                                   ", price[9], "$")

    print("")

menu()
a()


input()