import random_practise, Project

flights = ["Air Asia", "Vistara", "kingfisher"]

business_price = 10000
economy_price = 3000


def seat_booking(price, name, seats, booked, flight_name):
    print("Total price :- {0}".format(price * len(name)))
    print()
    print("Flight Name : - {0}".format(flight_name))
    for i in range(len(seats)):
        print("****  Ticket Number  ****: {0}  ".format(i + 1))
        print("      Name :- {0}".format(name[i]))
        print("      Seat No :- {0}".format(seats[i]))

        data = [name[i], seats[i], flight_name]
        booked.append(data)


def random_flight():
    return random_practise.choice(flights)


def print_seats(list):
    for i in range(len(list)):
        for j in range(len(list[0])):
            print("{0}{1} ".format(i, j), end="")
        print()


economy_class = [[[0 for i in range(3)] for j in range(20)] for k in range(2)]
business_class = [[[0 for x in range(1)] for y in range(10)] for z in range(2)]
economy_booked_data = []
business_booked_data = []


def seat_checker(list, row):
    seat_no = input("Enter Seat Number :- ")
    if len(seat_no) == 2:
        r = int(seat_no[0])
        c = int(seat_no[1])
    else:
        r = int(seat_no[0] + seat_no[1])
        c = int(seat_no[2])

    while list[row][r][c] == "*":
        seat_no = input("Enter valid Seat Number :- ")
        if (len(seat_no) == 2):
            r = int(seat_no[0])
            c = int(seat_no[1])
        else:

            r = int(seat_no[0] + seat_no[1])
            c = int(seat_no[2])
    list[row][r][c] = "*"
    return str(r) + str(c)

def make_plane():
    for i in range(4):
        for j in range (4):
            if i+j<=4 and i==j:
                print("*" , end = "")
            elif i == 3 and j == 1:
                print("*" , end = "")

            else:
                print(' ' , end = "")
        print()

def interFace():
    form = input("from :- ")
    to = input("To :- ")

    flight_name = random_flight()
    print("for booking in :")
    print("               Economy Class : 1")
    print("               Business Class : 2")
    section = input()
    print("In which raw you want to book seat 1 or 2 ")
    row = input()
    if section == "1":
        print_seats(economy_class[int(row) - 1])
        list = []
        seats = []
        seat_count = int(input("enter count of seats you want to book "))
        while seat_count != 0:
            seat_no = seat_checker(economy_class, int(row))
            seat_count -= 1
            name = input("Enter name for seat no {0} ".format(seat_no))
            list.append(name)
            seats.append(seat_no)
        seat_booking(economy_price, list, seats, economy_booked_data, flight_name)
        print("For :")
        print("    exit : -1")
        print("    continue : 1")
        command = input()
        if command == ("1"):
            interFace()
        else:
            Project.Customer()
    elif section == "2":
        print_seats(business_class[int(row)])
        list = []
        seats = []
        seat_count = int(input("enter count of seats you want to book "))
        while seat_count != 0:
            seat_no = seat_checker(business_class, int(row))
            seat_count -= 1
            name = input("Enter name for seat no {0} ".format(seat_no))
            list.append(name)
            seats.append(seat_no)
        seat_booking(business_price, list, seats, business_booked_data, flight_name)
        print("For :")
        print("    exit : -1")
        print("    continue : 1")
        command = input()
        if command == ("1"):
            interFace()
        else:
            Project.Customer()


def show_data_to_employ():
    print("for seeing data of business class press  1")
    print("for seeing data of Economy class press  2")
    response = input("Give your response :- ")
    if response == "-1":
        Project.call()
    if response == "1":
        print("-" * 20)
        for i in range(len(business_booked_data)):
            print("Name : - {0}".format(business_booked_data[i][0]))
            print("seat Number : - {0}".format(business_booked_data[i][1]))
            print("Flight Name: - {0}".format(business_booked_data[i][2]))
    elif response == "2":
        print("-" * 20)
        for i in range(len(economy_booked_data)):
            print("Name : - {0}".format(economy_booked_data[i][0]))
            print("seat Number : - {0}".format(economy_booked_data[i][1]))
            print("Flight Name: - {0}".format(economy_booked_data[i][2]))
        print("-" * 20)
    input("Press Any key for exit")
    Project.call()

