import sqlite3 as sql
import time
from nums_from_string import get_nums

conn = sql.connect(r'logs.sqlite3')


print("База данных успешно подключена")

c = conn.cursor()


def db_data(offset):
    user_strokes = []
    user_strokes_in_building = []
    cab_list = [800, 813, 814, 816, 818]
    home_users = ['user_3', 'user_6', 'user_12', 'user_1', 'user_13']
    count = 0
    c.execute("select * from logs_test limit 5 offset '{}'".format(offset))
    data_strokes = c.fetchall()
    for data_stroke in data_strokes:
        count = count + 1
        list_data_stroke = list(data_stroke)
        for cab in cab_list:
            try:
                if int(get_nums(str(list_data_stroke[2]))[0]) == cab:
                        print(list_data_stroke)
                        if list_data_stroke[5] != 105:
                            del list_data_stroke[3:5]
                            for user in home_users:
                                if user == str(list_data_stroke[1]):
                                    if list_data_stroke not in user_strokes:
                                        list_data_stroke.append('TRUE')
                                        user_strokes.append(list_data_stroke)
                                else:
                                    if list_data_stroke not in user_strokes:
                                        list_data_stroke.append('FALSE')
                                        user_strokes.append(list_data_stroke)
            except:
                pass
        try:
            if list_data_stroke[5] != 105:
                del list_data_stroke[3:5]
        except:
            pass
        for user in home_users:
            if user == str(list_data_stroke[1]):
                if list_data_stroke not in user_strokes:
                    if list_data_stroke not in user_strokes_in_building:
                        list_data_stroke.append('TRUE')
                        user_strokes_in_building.append(list_data_stroke)

    return user_strokes, count, user_strokes_in_building


def cash_bd(strokes, strokes_from_all_b):
    conn2 = sql.connect(r'cash_db.sqlite3')
    c2 = conn2.cursor()
    for stroke in strokes:
        if stroke[3] == 101:
            try:
                print('udalil')
                c2.execute("DELETE FROM users_on_9 where name='{}' and cab='{}' and  event_id='{}'")
                conn2.commit()
            except:
                pass
            c2.execute("replace into users_on_9 (id, name, cab, event_id, home_level) values (?,?,?,?,?)", stroke)
            conn2.commit()
        if stroke[3] == 102:
            try:
                c2.execute("DELETE FROM users_on_9 WHERE name='{}' and cab='{}'".format(stroke[1], stroke[2]))
                conn2.commit()
                # if stroke[2] == 814 or 813:
                #     c2.execute("replace into users_on_9 (id, name, cab, event_id) values (?,?,,?)", stroke)
                #     conn2.commit()
            except:
                print(stroke)
                pass
    if strokes_from_all_b:
        for stroke in strokes_from_all_b:
            if stroke[3] == 101:
                c2.execute("replace into users_from_9_in_build (id, name, cab, event_id, home_level) values (?,?,?,?,?)", stroke)
                conn2.commit()
            if stroke[3] == 102:
                try:
                    c2.execute("DELETE FROM users_from_9_in_build WHERE name='{}' and cab='{}'".format(stroke[1], stroke[2]))
                    conn2.commit()
                    # if stroke[2] == 814 or 813:
                    #     c2.execute("replace into users_on_9 (id, name, cab, event_id) values (?,?,,?)", stroke)
                    #     conn2.commit()
                except:
                    print(stroke)
                    pass
    conn2.close()





def main_db_test(x):

    offset = 0
    while True:
        time.sleep(x)
        strokes, offset1, data_in_b = db_data(offset)
        if offset1 != 0:
            offset = offset + offset1
        cash_bd(strokes, data_in_b)

main_db_test(6)