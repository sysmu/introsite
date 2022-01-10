import random


def random_number_of_workers():
    x = random.randrange(0, 5, 1)
    y = random.randrange(x, x+5 , 1)
    return x, y


def random_name():
    names = ['Ivan', 'Oleg', 'Elena', 'Anastasia', 'Valentina', 'Maks', 'Pavel', 'Sasha', 'Sergey','Evgenii', 'Vika']
    random_name = random.choice(names)
    return random_name


def check_rooms():
    cabs_on_9_floor = [900, 901, 902, 903, 904]
    cabs_on_other_floors = [701, 730, 729, 731]
    random_cab_on_9_floor = random.choice(cabs_on_9_floor)
    random_cab_on_other_floors = random.choice(cabs_on_other_floors)
    return random_cab_on_9_floor, random_cab_on_other_floors


def random_user_stroke(i):
    user_stroke = []
    random_user_name = str(random_name())
    random_cab = check_rooms()
    user_stroke.append(i)
    user_stroke.append(random_user_name)
    user_stroke.append(random_cab[0])
    return user_stroke


def stroke_with_align_cab(i,cab):
    user_stroke = []
    random_user_name = str(random_name())
    user_stroke.append(i)
    user_stroke.append(random_user_name)
    user_stroke.append(cab)
    return user_stroke
