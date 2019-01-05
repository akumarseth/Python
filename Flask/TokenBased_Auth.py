from flask import Flask, jsonify, request, make_response, redirect, url_for
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bshdsvhewje'

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token') #http://127.0.0.1:5000/route?token=alshfjfjdklsfj89549834ur
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is invalid!'}), 403
        return f(*args, **kwargs)

    return wrapper

@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'Anyone can view this!'})

@app.route('/protected')
@token_required
def protected():
    return jsonify({'message' : 'visible only for the user with valid tokens.'})

@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.username == 'Abhishek' and auth.password == 'Password':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=120)}, app.config['SECRET_KEY'])
        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

@app.route('/')
def index():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)