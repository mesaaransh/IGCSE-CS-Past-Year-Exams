import os

cabin_name = ["hetty", "poppy", "blue skies", "bay view", "Happy Days", "Summer Joy", "Walkers Rest", "Bertie", "Green Forest Lodge", "Coppice Lodge"]
cabin_capacity = ["4", "4", "4", "6", "6", "6", "8", "8", "10", "10"]
cabin_peak_cost = [400, 400, 500, 650, 695, 800, 950, 1050, 1200, 1500]
cabin_offpeak_cost = [250, 250, 300, 500, 550, 600, 750, 850, 950, 1150]

price = []
cabins = []
booked_cabins = [[], [], [], [], [], [], [], [], [], []]
booking_codes = [[], [], [], [], [], [], [], [], [], []]
ucode = 100
counter = 0

def mkzero():
    global counter
    del price[:]
    del cabins[:]
    counter = 0

def reprequest():

    urequest = input("You want more days to live in?")

    if urequest == "y":
        print()
        request()

    elif urequest == "n":
        print()
        print("your bookings", cabins)
        print("Cabin prices = ", price)
        print("total price = ", sum(price))

        if counter >= 3:
            disprice = (sum(price) - ((sum(price)/100)*10))
            print("discounted price = ", disprice)

        else:
            print("discount = 0")

        input()
        cls()
        reporder()

    else:
        print("invalid input")
        reprequest()

def reporder():

    a = input("next order?")

    if a == "y":
        mkzero()
        request()

    if a == "n":
        for t in range(3):
            reporder()

    else:
        reporder()

def request():

    cabin_booking = input("Which cabin do you want? ")
    cabins.append(cabin_booking)

    if cabin_booking in cabin_name:
        global cabin_number
        cabin_number = cabin_name.index(cabin_booking)
        global cabin_booking_week
        cabin_booking_week = int(input("for which week do you want to book? (23-39)"))

        booking_auth()
    else:
        print("input invalid")
        request()

def booking_auth():

    if cabin_booking_week < 23:
        print("Not available!!!!!")
        input()
        cls()
        request()

    elif cabin_booking_week > 39:
        print("Not available!!!!!")
        input()
        cls()
        request()

    booking_confo()

def booking_confo():

    global ucode
    global counter
    x = cabin_booking_week in booked_cabins[cabin_number]

    if x is False:
        booked_cabins[cabin_number].append(cabin_booking_week)
        print(booked_cabins)
        print("booking confirmed")
        booking_codes[cabin_number].append(ucode)
        print("Unique code = ", ucode)
        ucode = ucode + 1
        counter = counter + 1
        booking_price()
    else:
        print("NOT AVAILABLE")
        request()

def booking_price():
    if cabin_booking_week >= 27 and cabin_booking_week <= 35:
        price.append(cabin_peak_cost[cabin_number])

    elif cabin_booking_week >= 23 and cabin_booking_week <= 26 or cabin_booking_week >= 36 and cabin_booking_week <= 39:
        price.append(cabin_offpeak_cost[cabin_number])

    reprequest()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

print(cabin_name)
request()