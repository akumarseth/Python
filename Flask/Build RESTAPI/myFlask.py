from flask import Flask
import os
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

@app.route('/')
def hello_world():
    # sum = 10 + 20
    return basedir


if __name__ == '__main__':
    app.run()