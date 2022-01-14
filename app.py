from flask import Flask, render_template
from for_workers import main
import sqlite3 as sql

app = Flask(__name__)

def check(users9, on_floor, stroke):
    if users9 == 0:
        if on_floor == 0:
            return "Никого нет на этаже"
        else:
            c = db_work()
            data = c.execute('select id,  name, cab  from users_from_9_in_build order by id desc  limit 1').fetchall()
            if data == 0:
                return "Закройте этаж"
            else:
                for id, name, cab in data:
                    name = name
                    cab = cab
                return "Что бы закрыть этаж обратитесь к " + name + " в " + cab

    elif users9 >= 2:
        if on_floor >= 2:
            return "Все хорошо, этаж не нужно закрывать"
        else:
            for data in stroke:
                if data[2] == 'TRUE':
                    cab = data[1]
            return "Работник с 9 этажа в " + str(cab)
    else:
        if on_floor == 1:
            return "Вы последний"
        elif on_floor == 2:
            for data in stroke:
                if data[2] == 'TRUE':
                    cab = data[1]
                    return "Работник с другого этажа в " + str(cab)
        else:
            for data in stroke:
                if data[2] == 'TRUE':
                    cab = data[1]
                    return "Работник с 9 этажа в " + str(cab)



def db_work():
    conn2 = sql.connect(r'cash_db.sqlite3')
    return conn2


@app.route('/')
def hello_world():  # put application's code here
    on_level_from_9 = 0
    counter = 0
    id = []
    id.clear()
    c = db_work()
    data = c.execute('select name, cab, home_level from users_on_9').fetchall()
    print(data)
    for stroke in data:
        counter = counter + 1
        id.append(counter)
    for n, co, h in data:
        if h == 'TRUE':
            print(h)
            on_level_from_9 = on_level_from_9 + 1
    print(on_level_from_9)
    message = check(on_level_from_9,counter, data)
    c.close()

    return render_template('home_page_db.html', data=enumerate(data, start=1), on_floor=counter, from_other_level= counter - on_level_from_9, message=message)


@app.route('/random')
def hello_random():  # put application's code here
    response, workers_on_floor, list_of_workers, workers_from_other_level = main()
    return render_template('home_page.html', on_floor=workers_on_floor, list=list_of_workers, message=response, others=workers_from_other_level)


if __name__ == '__main__':
    app.run()
