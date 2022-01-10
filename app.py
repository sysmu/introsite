from flask import Flask, render_template
import datetime
from for_workers import main

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    response, workers_on_floor, list_of_workers = main()
    return render_template('home_page.html', on_floor=workers_on_floor, list=list_of_workers, message=response)


def handler_landing():
    return str(datetime.datetime.now())


if __name__ == '__main__':
    app.run()
