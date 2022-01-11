import sqlite3 as sql
import time

conn = sql.connect(r'logs.sqlite3')


print("База данных успешно подключена")

c = conn.cursor()



def db_data(offset):
    user_strokes = []
    count = 0
    c.execute("select * from logs_test limit 4 offset '{}'".format(offset))
    data_strokes = c.fetchall()
    print(data_strokes)
    for data_stroke in data_strokes:
        count = count + 1
        list_data_stroke = list(data_stroke)
        if list_data_stroke[5] != 105:
            del list_data_stroke[3:5]
            user_strokes.append(list_data_stroke)
    return user_strokes, count


def cash_bd(strokes):
    conn2 = sql.connect(r'cash_db.sqlite3')
    c2 = conn2.cursor()
    for stroke in strokes:
        if stroke[3] == 101:
            c2.execute("replace into users_on_9 (id, name, cab, event_id) values (?,?,?,?)", stroke)
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
    conn2.close()





def main_db_test(x):
    offset = 0
    while True:
        time.sleep(x)
        strokes, offset1 = db_data(offset)
        if offset1 != 0:
            offset = offset + offset1
        cash_bd(strokes)

main_db_test(6)