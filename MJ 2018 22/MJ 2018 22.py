import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

stock_processor = []
p3 = int(input("enter p3 stocks"))
p5 = int(input("enter p5 stocks"))
p7 = int(input("enter p7 stocks"))
print()
stock_processor.append(p3)
stock_processor.append(p5)
stock_processor.append(p7)

stock_ram = []
gb16 = int(input("enter 16gb ram stocks"))
gb32 = int(input("enter 32gb ram stocks"))
print()
stock_ram.append(gb32)
stock_ram.append(gb16)

stock_storage = []
tb1 = int(input("enter 1tb rom stocks"))
tb2 = int(input("enter 2tb rom stocks"))
print()
stock_storage.append(tb1)
stock_storage.append(tb2)

stock_ports = []
ports2 = int(input("enter 2 usb stocks"))
ports4 = int(input("enter 4 usb stocks"))
print()
stock_ports.append(ports2)
stock_ports.append(ports4)

stock_screen = []
inches19 = int(input("enter 19 inches stocks"))
inches23 = int(input("enter 23 inches stocks"))
print()
stock_screen.append(inches19)
stock_screen.append(inches23)

stock_case = []
mini = int(input("enter mini tower stocks"))
midi = int(input("enter midi tower stocks"))
print()
stock_case.append(mini)
stock_case.append(midi)

cls()


price = 0
print()
print("                                                         enter your requirements of computer")
processor = input("enter type of processor(p3,p5,p7):")
if all([processor == "p3", p3 >= 1]):
    price = price + 100
    p3 = p3-1
elif all([processor == "p5", p5 >= 1]):
    price = price + 120
    p5 = p5 - 1
elif all([processor == "p7", p7 >= 1]):
    price = price + 200
    p7 = p7 - 1
else:
    print("input not valid")

ram = input("enter type of ram (16,32):")
if all([ram == "16" , gb16 >= 1]):
    price = price + 75
    gb16 = gb16 - 1
elif all([ram == "32" , gb32 >= 1]):
    price = price + 150
    gb32 = gb32 - 1
else:
    print("input not valid")

storage = input("enter type of storage (1tb,2tb):")
if all([storage == "1tb" , tb1 >= 1]):
    price = price + 50
    tb1 = tb1 - 1
elif all([storage == "2tb" , tb2 >= 1]):
    price = price + 100
    tb2 = tb2 - 1
else:
    print("input not valid")

screen = input("enter type of screen (19in, 23in)")
if all([screen == "19in" , inches19 >= 1]):
    price = price + 65
    inches19 = inches19 - 1
elif all([screen == "23in" , inches23 >= 1]):
    price = price + 120
    inches23 = inches23 - 1
else:
    print("input not valid")

case = input("enter type of case(mini,midi):")
if all([case == "mini" , mini >= 1]):
    price = price + 40
    mini = mini - 1
elif all([case == "midi" , midi >= 1]):
    price = price + 70
    midi = midi - 1
else:
    print("input not valid")

ports = input("enter number of ports(2,4):")
if all([ports == "2" , ports2 >= 1]):
    price = price + 10
    ports2 = ports2 - 1
elif all([ports == "4" , ports4 >= 1]):
    price = price + 20
    ports4 = ports4 - 1
else:
    print("input not valid")

total_price = price + (price/100 * 20)
print()
print("price estimate = ", round(total_price))

cls()

flow = input("next order?? ")