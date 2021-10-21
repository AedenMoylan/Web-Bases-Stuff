from flask import Flask

import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return datetime.datetime.now().ctime()


@app.route("/hello")
def hello():
    return "hello bababooey"


if __name__=="__main__":
    app.run()