import os


cars = ["Hatchback", "Saloon", "Estate"]
car_price = [535000, 495000, 625000]
extras = ["Luxury seats", "satellite navigation", "parking sensors", "Bluetooth connectivity", "sound system"]
extras_price = [45000, 5500, 10000, 350, 1000]
trade_ammount = 0
customer_car = ""
required_extras = []
required_extras_price = []
required_car_price = 0
discount_var = 1


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


print(cars)
x = 1
while x > 0:  # input of car model
    customer_car = input("which car you want? ")
    if customer_car in cars:
        print(customer_car + " has been booked")
        required_car_price = car_price[cars.index(customer_car)]
        x -= 1
    else:
        print("invalid Input")

print("")
print("how many extras you want?")

x = 1
while x > 0:  # input of extras
    no_optional_extras = int(input(
        "from: Luxury seats(1), satellite navigation(2), parking sensors(3), Bluetooth connectivity(4), sound system(5)"))
    if len(extras) >= no_optional_extras >= 0:
        while no_optional_extras > 0:
            optional_extra = int(input("Name index of one extra: "))
            required_extras.append(extras[optional_extra - 1])
            required_extras_price.append(extras_price[optional_extra - 1])
            print("You have booked these extras: ", required_extras)
            no_optional_extras -= 1
        x -= 1
    else:
        print("invalid option")

total_extra_price = sum(required_extras_price)
final_price = total_extra_price + required_car_price

old_car = input("Do you have an old car to trade in: ")
x = 1
while x > 0:
    if old_car == "Y":
        trade_ammount = int(input("input discount ammount: "))
        if trade_ammount < 10000 or trade_ammount > 100000:
            print("invalid Input")
        else:
            break
    else:
        discount_var -= .05
        break

old_customer = input("Are you an old customer(Y/N)? ")

if old_customer == "Y":
    print("Congrats! You get a 10% discount")
    discount_var -= 0.1

input()
cls()

# Task 1
# ---------------------------------------------------------------------
# Task 2


def bill():
    print("")
    print("")
    print("booked car: ", customer_car)

    print("")
    print("Booked Extras: ", required_extras)
    print("price of booked extras: ", required_extras_price)
    print("total extra price: ", total_extra_price)
    print("")
    print("Base Ammount: ", required_car_price)
    global final_price
    print("Your Ammount: ", final_price)
    print("")
    print("***discounts***")
    print("For an old car: -", trade_ammount)
    print("Generous discounts: -", 100 - discount_var * 100, "%")
    print("")
    final_price = final_price - trade_ammount
    final_price *= discount_var
    print("You need to pay: ", final_price)
bill()

pay_method = input("Select Payment Method: ")
print("")
if pay_method == "1":
    print("You get a 1% cashback(1) or the optional extras free(2):")
    cashback = round(final_price * .01, 2)

    if total_extra_price >= cashback:
        print("***Best Value***")
        print("Take the extras free worth ", total_extra_price)
        final_price -= total_extra_price
        print("Final value: ", final_price)

        print("")

        print("***alternate Value***")
        print("Take the cashback: ", cashback)
        final_price = (final_price + total_extra_price) - cashback
        print("Final value: ", final_price)

    else:
        print("***Best Value***")
        print("Take the cashback: ", cashback)
        final_price -= cashback
        print("Final value: ", final_price)

        print("")

        print("***alternate Value***")
        print("Take the extras free worth ", total_extra_price)
        final_price = (final_price + cashback) - total_extra_price
        print("Final value: ", final_price)

    pay_method_2 = input("Which one you chose: ")
    cls()

    if pay_method_2 == "1":
        print("Take the cashback: ", cashback)
        final_price -= cashback
        print("Final value: ", final_price)

    if pay_method_2 == "2":
        print("Take the extras free worth ", total_extra_price)
        final_price -= total_extra_price
        print("Final value: ", final_price)

elif pay_method == "2":
    print("You make payments in next 4 yrs")
    print("Number of payments: 48")
    print("final ammount: ", round(final_price, 2))
    print("payment per installment(1month): ", round(final_price / 48, 2))

elif pay_method == "3":
    print("you get a 5% interest for installments in next 7 yrs")
    final_price *= 1.05
    print("Number of payments: 84")
    print("resultant ammount: ", round(final_price, 2))
    print("payment per installment(1month): ", round(final_price / 84, 2))

else:
    print("invalid option")

