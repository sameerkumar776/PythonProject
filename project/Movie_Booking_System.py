import Common_Use_Methode
import Project

movie_list = ["Avatar 2", "Chup", "Sutter Iland"]
## we use 3d list in this i will store movie position and j will store rol number and i will store row number
seats = [[[" " for k in range(9)] for j in range(9)] for i in range(len(movie_list))]
detail = [[[" " for z in range(9)] for y in range(9)] for x in range(len(movie_list))]
stars = [3, 4, 5]
place = ["Dera Bassi", "Zerakpur", "Mohali"]
price = [200, 250, 300]
count = 1
booked_seat = [[] for o in range(len(movie_list))]


def show_movie_list_diagram():
    global count

    longest_1 = Common_Use_Methode.find_max_len(movie_list)
    longest_2 = Common_Use_Methode.find_max_len(stars) + 8
    longest_3 = Common_Use_Methode.find_max_len(place) + 8
    last = max(longest_1, max(longest_2, longest_3))
    print("_" * 30)

    for i in range(len(movie_list)):
        print("{0}.".format(count), end="")
        print("||{0}||".format(movie_list[i].center(last + 6, " ")))
        print("  ||{0}".format("Rating :{0}".format(Common_Use_Methode.rating_string(stars[i])).center(last + 4, " ")),
              end="")

        print("  ||")

        print("  ||{0}||".format("Place : {0}".format(place[i]).center(last + 6, " ")))
        print("  Price : Rs.{0}".format(price[i]))
        print("_" * 30)
        count = count + 1


def movieList():
    show_movie_list_diagram()
    movie_name = input("Enter Which Movie You Want to See (Give Position Number) : ")
    if (movie_name == "-1"):
        Project.Customer()
    else:
        tickets = input("How Ticket you want to Buy of {0} ".format(movie_list[int(movie_name) - 1]))

        MovieSeats(seats[int(movie_name) - 1])
        seat_book(seats[int(movie_name) - 1], int(tickets), movie_list[int(movie_name) - 1], price[int(movie_name) - 1],
                  place[int(movie_name) - 1], movie_name,
                  detail[int(movie_name) - 1])


def MovieSeats(booking):
    print(" **** filled by denoted by * ")
    count = 1
    booking[8][1] = "*"

    print("-" * 30)
    for i in range(9):
        if i == 0:
            for j in range(0, 6):
                if j != 0:
                    if booking[i][j] == "*":
                        print("*  ", end="")
                    else:
                        print("{0}{1} ".format(i, j), end="")
                    count += 1
                else:
                    print("   ", end="")
            print("{0}{1}".format(" " * 17, "|"), end="")

            print()
        else:
            for j in range(9):
                if j != 4:
                    if booking[i][j] == "*":
                        print("*  ", end="")
                    else:
                        print("{0}{1} ".format(i, j), end="")
                    count += 1
                else:
                    print(" ", end="")
            print("{0}{1}".format(" " * 10, "|"), end="")

            print()
    print("-" * 30)


def ticketPrint(user_list, movie_name, timing, seats, price, place):
    print(" " * 20, end="")
    print("-" * 20)
    print(" " * 20, end="")
    print("Film Name : {0}".format(movie_name))
    for i in range(len(user_list)):
        print(" " * 20, end="")
        print("{0} Seat No: {1}".format(user_list[i], seats[i]))
    print(" " * 20, end="")
    print("Time : {0}".format(timing))
    print("{0}Place : {1}".format(" " * 20, place))
    print("{1}Toatal Price : {0}".format(price * len(user_list), " " * 20))
    print(" " * 20, end="")
    print("-" * 20)


def seat_book(booking, count, movie_name, price, place, movie_position, data):
    for i in range(count):

        while True:
            row = int(input("Row Number : "))
            col = int(input("Column Number : "))
            if booking[row][col] != '*':
                booking[row][col] = "*"

                break
            else:
                print("this seat is already filled please select another one")
        booked_seat[int(movie_position) - 1].append("{0}{1}".format(row, col))
    user_data = []
    for i in (booked_seat[int(movie_position) - 1]):
        name = input("Enter Name Ticket {0} : ".format(i))
        user_data.append(name)

        data[int(i[0])][int(i[1])] = name
    ticketPrint(user_data, movie_name, "9:00 PM", booked_seat[int(movie_position) - 1], price, place)
    print("For exit press (-1)")
    print("For continue Shopping press (1)")
    ans = input()
    if ans == "-1":
        import Project
        Project.Customer()
    else:
        movieList()


def details():
    global count
    longest_1 = Common_Use_Methode.find_max_len(movie_list)
    longest_2 = Common_Use_Methode.find_max_len(stars) + 8
    longest_3 = Common_Use_Methode.find_max_len(place) + 8
    last = max(longest_1, max(longest_2, longest_3))
    print("Details of :")
    for i in range(len(movie_list)):
        print("{0}.".format(count), end="")
        print("||{0}||".format(movie_list[i].center(last + 6, " ")))
        print("  ||{0}".format("Rating :{0}".format(Common_Use_Methode.rating_string(stars[i])).center(last + 4, " ")),
              end="")

        print("  ||")

        print("  ||{0}||".format("Place : {0}".format(place[i]).center(last + 6, " ")))
        print("  Price : Rs.{0}".format(price[i]))
        print("_" * 30)
        count = count + 1


def show_details_toEmploy(data, position):
    print("-" * 20)
    space = " " * 15
    print(" Seat no:{0}Names".format(space))
    for i in data:
        print("  {0}{1}{2}".format(i, space, detail[position][int(i[0])][int(i[1])]))
    recall()


def recall():
    k = input("For exit press -1 and for continue press 1")
    if k == "-1":
        Project.InterFace()
    else:
        Project.call()


def find_number_of_booked_ticket(position):
    booked = booked_seat[position]

    option = input("for checking seats : 1")
    if option == "1":
        if len(booked) > 0:
            show_details_toEmploy(booked, position)
        else:
            print("------No seats Booked yet----")
            recall()
