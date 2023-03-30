import Movie_Booking_System as MOVE_SYSTEM
import Food_Delivery_System , flight_ticket_booking

times = 0
spaces = "\t"


def Customer():
    list = ["Movie Ticket Press(1)", "Flight Ticket Press(2)", "Food Ordering  Press(3)"]
    word = "For Buying : "
    print(word)
    for i in list:
        print("{1}-> {0}".format(i, " " * len(word)))
    command = input("What you Want to Book ??\n")

    if command == "3":
        Food_Delivery_System.Service()
    elif command == "1":
        MOVE_SYSTEM.movieList()
    elif command == "-1":
        InterFace()
    elif command == "2":
        flight_ticket_booking.interFace()


def findUser(Name, User_name_list):
    for i in range(len(User_name_list)):
        if Name == User_name_list[i]:
            return i
    return -1


def employ():
    Name = ["2210990776", "2210990761", "2210990777"]
    password = ["776", "761", "777"]
    index = -1
    n = 4
    while index == -1:
        user_name = input("User ID = ")
        index = findUser(user_name, Name)
        if index == -1:
            print("***  Wrong User ID ***")
            if n == 0:
                n = 4
                print("Try After 1 min")
                digit_1 = 6
                digit_2 = 0

                while digit_1 + digit_2 != 0:
                    if digit_2 == 0:
                        print("{0}{1} seconds left".format(digit_1, digit_2))
                    i = 10000000
                    while i != 0:
                        i = i - 1
                    digit_1 = digit_1 - 1

        n -= 1
    else:
        current_password = password[index]
    enter_password = input(" ****  Password = ")
    if current_password == enter_password:
        call()
    else:
        print("wrong password \nenter again")
def call():

        print("To Check Detail :")
        print("{0}Of FLIGHT Booking --> 0".format(spaces * 2))
        print("{0}Of Movie Ticket Booking -->1".format(spaces * 2))
        print("{0}Of Food Order -->2".format(spaces * 2))
        ans = input()
        if ans == "1":

            MOVE_SYSTEM.show_movie_list_diagram()
            value = input("Enter Position Movie to see details:")
            MOVE_SYSTEM.find_number_of_booked_ticket(int(value)-1)
        elif ans == "2":
            Food_Delivery_System.show_details()
        elif ans == "0":
            flight_ticket_booking.show_data_to_employ()



def InterFace():
    name = "Booking System"

    print("{1}Welcome to {0}  ".format(name, spaces * 50))

    print("\n{0}Login as Customer or Employee "
          "\n{1}for login as customer enter 1 "
          "\n{2}for login as employee enter 2".format(spaces * 5, spaces * 5, spaces * 5))
    print("for going back press -1")

    user = input("Login ")
    if user == "2":

        employ()
    elif user == "1":

        Customer()
    else:
        exit()


if __name__ == "__main__":

    InterFace()
