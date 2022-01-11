from generate_random_workers import *


def check(users9, on_floor):
    cab_from_9, others_cab = check_rooms()
    if users9 == 0:
        if on_floor == 0:
            return "nothing to see", 0
        else:
            return "Close the floor", 0
    elif users9 >= 2:
        if on_floor >= 2:
            return "all is ok", 0
        else:
            return "the align is in " + str(cab_from_9) + " cab", cab_from_9
        # else:
        #     return "the last man is in " + str(others_cab) + " cab", others_cab
    else:
        if on_floor == 1:
            return "u r the last one", 0
        elif on_floor == 2:
            return "the align is in " + str(cab_from_9) + " cab", cab_from_9
        else:
            return "man from 9 floor is in " + str(cab_from_9) + " cab", cab_from_9


def main():
    while True:
        user_stroke = []
        user9, on_floor = random_number_of_workers()
        print("workers on the 9 floor: " + str(on_floor) + '\n', "workers from 9 in building: " + str(user9) + '\n',
              "workers from others levels: " + str(on_floor - user9))
        message, cab = check(user9, on_floor)
        print(message)
        if user9 == 1 and on_floor != 2:
            i = int(on_floor) - 1
        else:
            i = int(on_floor)
        c = 1
        while i != 0:
            test = random_user_stroke(c)
            user_stroke.append(test)
            i = i - 1
            c = c + 1
        if cab != 0:
            test1 = stroke_with_align_cab(c, cab)
            user_stroke.append(test1)
        print(user_stroke)
        return message, on_floor, user_stroke
