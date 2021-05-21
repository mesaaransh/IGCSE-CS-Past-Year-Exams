print ("                                     ------- Packaging servers")
print()
print()
print()


parcel = input("enter no. of parcels in a consingment : ")
accepted = int(parcel)
status = "accepted"
total_weight = 0
total_price = 0
rejected = 0
count = 1


while count <= int(parcel):
    print ()
    print("parcel no.", count)
    print()
    dem_1 = input("enter 1st dimension(cm): ")
    dem_2 = input("enter 2nd dimension(cm): ")
    dem_3 = input("enter 3rd dimension(cm): ")
    print()
    weight = input("enter weight of parcel(Kg): ")
    print()

    if float(dem_1) >= 81:
        print("dimension 1 > 80")
        status = "rejected"

    if float(dem_2) >= 81:
        print("dimension 2 > 80")
        status = "rejected"

    if float(dem_3) >= 81:
        print("dimension 3 > 80")
        status = "rejected"

    if float(weight) < 1:
        print("weight too less")
        status = "rejected"

    if float(weight) > 10:
        print("item is too heavy")
        status = "rejected"

    if float(dem_1) + float(dem_2) + float(dem_3) >= int(200):
        print("Dimensions are larger than expected")
        status = "rejected"

    if status == "rejected":
        rejected = rejected + 1

    if status == "accepted":
        if float(weight) <= 5:
            print("price = 10$")
            total_price = total_price + 10

        if float(weight) > 5:
            print("price = ", (float(weight) - 5) + 10, "$")
            total_price = total_price + (float(weight) - 5) + 10

        total_weight = total_weight + float(weight)


    print("status = ", status)
    print()
    print()
    count = count + 1
    accepted = int(parcel) - rejected
    status = "accepted"



print()
print()
print()
print("                                     TOTAL CONSINGMENT")
print("total parcels : ", count - 1)
print("parcels rejected : " , rejected)
print("parcels accepted : ", accepted)
print("total price of consingment: ", total_price,"$")
print("total weight of consingment: ", total_weight,"Kg")

input()