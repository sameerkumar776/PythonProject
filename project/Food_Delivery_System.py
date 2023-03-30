from Common_Use_Methode import find_max_len, rating
import Project

booked_person_data = []
address = []
food_list = ["curry , rice", "Rajma Chawal", "Dalmakhni Rooti", "Chaola Bhatura", "Masla Dosa"]

food_list_2 = ["Non Veg Biryani", "Tanduri Chicken", "Seak Kabbab"]


def making_bill(order_list, price):
    print("\t" * 10, end="")
    size = find_max_len(order_list)
    print("-" * (size + 40))
    count = 1
    total_amount = 0
    for i in range(len(order_list)):
        print("{1}{2}. {0}: Rs.{3}".format(order_list[i], "\t" * 12, count, price[i]))
        count += 1
        total_amount = total_amount + price[i]

    print("{1}Total Bill : Rs.{0}".format(total_amount, "\t" * 13))
    print("\t" * 10, end="")
    print("-" * (size + 40))


def taking_user_data_for_Delivery():
    user_data = [input("Name : "), input("Phone Number : "), input("Address : ")]
    address.append(user_data)
    print("\t" * 10, end="")
    size = find_max_len(user_data)
    print("-" * (size + 40))
    type = ["Name", "Phone Number", "Address"]
    for i in range(len(user_data)):
        print("{0}{2} : {1}".format("\t" * 12, user_data[i], type[i]))
    print("{0}Delivery Time : 30 min".format("\t" * 12))
    print("\t" * 10, end="")
    print("-" * (size + 40))


def cancel_or_not(food_data):
    print("For Canceling order enter 0\nFor conforming order enter 1")
    command = int(input())
    if command == 0:

        Service()
    else:

        booked_person_data.append(food_data)
        taking_user_data_for_Delivery()
    print("For continue Shopping enter 1 \nFor exist enter -1")
    type = input()
    if 1 == int(type):
        Service()
    else:
        Project.Customer()


def takingOrder(menu_list, price):
    print("Please Enter Count of food you want to order")

    count = int(input())
    if count == -1:
        Service()
    order = []
    done = 1
    for i in range(count):
        position = input("Enter food number {0}: ".format(done))

        order.append(menu_list[int(position) - 1])
        done += 1

    making_bill(order, price)
    cancel_or_not(order)


def Service():
    print("--------Enter To Luch Service ---------")

    prince1 = [123, 143, 150, 80, 90]
    prince2 = [100, 200, 300]
    rating1 = [3, 4, 5, 1, 3]
    rating2 = [1, 2, 4]
    restraint_name = ["Aroma", "Aman Hotel", "Evergreen Hotel ", "", ""]
    type = input("\nFor (veg only) type --> 0"
                 " \nFor (non veg) only type --> 1 "
                 "\nFor both type --> 2\n")

    print("Food List ->\n")
    print(" -" * 20)
    if type == "0":
        for i in range(len(food_list)):
            max_len = find_max_len(food_list)
            print("|")
            print("| {0}{2} = Rs.{1}".format(food_list[i], prince1[i], " " * (max_len - len(food_list[i]) + 3)))
            print("| Rating : ", end="")

            rating(rating1[i])
            print()
            print("| Place : {0}".format(restraint_name[i]))
            print("| ", end="")
            print("-" * 10, end="\n")
        takingOrder(food_list, prince1)

    elif type == "1":
        for i in range(len(food_list_2)):
            max_len = find_max_len(food_list_2)
            print("| {0}{2} = Rs.{1}".format(food_list_2[i], prince2[i], " " * (max_len - len(food_list_2[i]) + 3)))
            print("| Rating : ", end="")

            rating(rating1[i])
            print()
            print("| Place : {0}".format(restraint_name[i]))
            print("| ", end="")
            print("-" * 10, end="\n")
        takingOrder(food_list_2, prince2)
    elif type == "2":
        t1 = find_max_len(food_list)
        t2 = find_max_len(food_list_2)
        max_len = max(t1, t2)
        for i in range(len(food_list)):
            print("| {0}{2} = Rs.{1}".format(food_list[i], prince1[i], " " * (max_len - len(food_list[i]) + 3)))
            print("| Rating : ", end="")
            rating(rating1[i])
            print()
            print("| Place : {0}".format(restraint_name[i]))
            print("| ", end="")
            print("-" * 10, end="\n")
        for i in range(len(food_list_2)):
            print("| {0}{2} = Rs.{1}".format(food_list_2[i], prince2[i], " " * (max_len - len(food_list_2[i]) + 3)))
            print("| Rating : ", end="")
            rating(rating2[i])
            print()
            print("| Place : {0}".format(restraint_name[i]))
            print("| ", end="")
            print("-" * 10, end="\n")
        takingOrder(food_list + food_list_2, prince1 + prince2)
    else:
        Project.Customer()
    print(" -" * 20)


def string_maker(list):
    string = ""
    i = 0
    for j in (list):
        if i == 0:
            string = string + j
            i = i + 1
        else:
            string = string + ", " + j
    return string


def show_details():
    if len(address) == 0:
        print("No booking yet")
        input("Enter -1 for go back")
        Project.call()
        return

    print("_" * 30)
    print("{0}{1}{2}".format(" Food List ", " " * 20, "User Data"))
    for i in range(len(address)):
        order_list = string_maker(booked_person_data[i])
        address_list = string_maker(address[i])

        print("{0}{1}{2}".format(order_list, " " * 2, address_list))
    input("Enter -1 for go back")
    Project.call()
