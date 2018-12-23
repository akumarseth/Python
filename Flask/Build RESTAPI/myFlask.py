from flask import Flask

app = Flask(__name__)

@app.route('/index/<Id>')
def hello_world(Id):
    sum = 10 + 20
    return Id + str(sum) + 'Hello World'


if __name__ == '__main__':
    app.run()