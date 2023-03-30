def rating_string(times):
    return "* " * times


def rating(stars):
    for i in range(stars):
        print("*", end=" ")


def find_max_len(dish):
    size = 0
    for i in dish:
        i = str(i)
        if size < len(i):
            size = len(i)
    return size
