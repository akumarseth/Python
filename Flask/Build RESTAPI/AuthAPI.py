from flask import Flask, jsonify, request, Response

from BookModel import *
import json
import jwt, datetime

from settings import *
from UserModel import *
from functools import wraps

books = Book().get_all_books()

app.config["SECERET_KEY"] = "meow"

@app.route('/login', methods=['POST'])
def get_token():
    request_data = request.get_json()
    username = request_data['username']
    password= request_data['password']

    match = User.username_password_match(username, password)
    if match:
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
        token = jwt.encode({'exp': expiration_date}, app.config["SECERET_KEY"], algorithm='HS256')
        return token
    else:
        return Response('', 401, mimetype='application/json')

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        try:
            jwt.decode(token, app.config['SECERET_KEY'])
            return f(*args, **kwargs)
        except:
            return jsonify({'error': 'Need a valid token to view this page'}), 401
    return  wrapper


# GET /books
@app.route('/books')
def get_books():
    return jsonify({'books': books})

@app.route('/books', methods=['POST'])
@token_required
def add_books():
    request_data = request.get_json()
    if(validBookObj(request_data)):
        new_book = {
            'name':request_data['name'],
            'price': request_data['price'],
            'isbn':request_data['isbn']
        }
        books.insert(0,new_book)
        response = Response("",201, mimetype="application/jsom")
        response.headers['Location'] = "/books"+ str(new_book['isbn'])
        return response
    else:
        invalid_obj = {
            "error": "invalid book object passed in request",
            "helpString": "Data passed in similar to this {'name':'Name', 'price': 59.09,'isbn':43234}"
        }
        response = Response(json.dumps(invalid_obj),400, mimetype="application/json")
        return response

@app.route('/books/<int:isbn>')
@token_required
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'name':book['name'],
                'price' : book['price']
            }
    return jsonify(return_value)

@app.route('/books/<int:isbn>', methods=['PUT'])
@token_required
def replace_book(isbn):
    request_data = request.get_json()
    if(not valid_put_request_data(request_data)):
        invalid_obj = {
            "error": "valid book object must be passed in request",
            "helpString": "Data passed in similar to this {'name':'Name', 'price': 59.09}"
        }
        response = Response(json.dumps(invalid_obj), 400, mimetype="application/json")
        return response

    new_book = {
        'name': request_data['name'],
        'price': request_data['price'],
        'isbn': isbn
    }
    i=0
    for book in books:
        currentIsbn = book["isbn"]
        if currentIsbn == isbn:
            books[i] = new_book
        i += 1
    response = Response("", status=204)
    return response

@app.route('/books/<int:isbn>', methods=['PATCH'])
@token_required
def update_book(isbn):
    request_data = request.get_json()
    updated_book = {}
    if "name" in request_data:
        updated_book["name"] = request_data['name']
    if "price" in request_data:
        updated_book["price"] = request_data['price']
    for book in books:
        if(book["isbn"]== isbn):
            book.update(updated_book)
    response = Response("", 204, mimetype="application/jsom")
    response.headers['Location'] = "/books" + str(isbn)
    return response

@app.route('/books/<int:isbn>', methods=['DELETE'])
@token_required
def delete_book(isbn):
    if(Book.delete_book(isbn)):
        response = Response("", status=204)
        return response
    invalidBookObjectErrorMsg = {
        "error":"Book with the ISBN number that was provided was not found so therefore unable to delete"
    }
    response = Response(json.dumps(invalidBookObjectErrorMsg), status=404, mimetype='applcation/json')
    return response

# # GET /books
# @app.route('/books')
# def get_books():
#     token = request.args.get('token')
#     try:
#         jwt.decode(token, app.config['SECERET_KEY'])
#     except:
#         return jsonify({'error': 'Need a valid token to view this page'}), 401
#
#     return jsonify({'books': books})

app.run(port=5000)