from flask import Flask, render_template
from for_workers import main
import sqlite3 as sql

app = Flask(__name__)


def db_work():
    conn3 = sql.connect(r'cash_db.sqlite3')
    return conn3


@app.route('/')
def hello_world():  # put application's code here

    counter = 0
    id = []
    id.clear()
    c = db_work()
    data = c.execute('select name, cab from users_on_9').fetchall()
    print(data)
    for stroke in data:
        counter = counter + 1
        id.append(counter)
    c.close()
    # response, workers_on_floor, list_of_workers = main()
    # return render_template('home_page.html', on_floor=workers_on_floor, list=list_of_workers, message=response)
    return render_template('home_page_db.html', data=enumerate(data, start=1), on_floor=counter)


@app.route('/random')
def hello_random():  # put application's code here
    response, workers_on_floor, list_of_workers = main()
    return render_template('home_page.html', on_floor=workers_on_floor, list=list_of_workers, message=response)


if __name__ == '__main__':
    app.run()
