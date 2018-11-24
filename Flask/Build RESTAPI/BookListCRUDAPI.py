from flask import Flask, jsonify, request,Response
import json
import jwt, datetime

app = Flask(__name__)
DEFAULT_PAGE_LIMIT = 3

books = [
    {
        'name':'Green Eggs and Ham',
        'price': 7.99,
        'isbn':5001
    },
    {
        'name':'Half girlfriend',
        'price': 6.99,
        'isbn':5002
    }
]

# GET /books/pagw/<int:page_number
# /books/page/1?limit=100
def get_paginated_books(page_number):
    print(type(request.args.get('limit')))
    LIMIT = request.args.get('limit', DEFAULT_PAGE_LIMIT)
    startIndex= page_number * LIMIT - LIMIT
    endIndex= page_number * LIMIT
    print(startIndex)
    print(endIndex)
    return jsonify({'books':books[startIndex:endIndex]})

# GET /books
@app.route('/books')
def get_books():
    return jsonify({'books': books})

# POST /books
# {
#     'name':'F',
#     'price': 5.99,
#     'isbn':5003
# }

def validBookObj(bookObject):
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return  False

def valid_put_request_data(bookObject):
    if ("name" in bookObject and "price" in bookObject):
        return True
    else:
        return  False

@app.route('/books', methods=['POST'])
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
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'name':book['name'],
                'price' : book['price']
            }
    return jsonify(return_value)

# PUT /books/5003
# {
#     'name':'Harry Poter',
#     'price':20.50
# }
# (1) no valid book onbject from our client
#  -> not add the boook to the store

# valid book object has name  and price field

# (2)no valid book object

@app.route('/books/<int:isbn>', methods=['PUT'])
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
# PATCH   /books/5011
# {
#     'name': 'Harry Potter and the Chamber of secrets'
# }

# PATCH  /books/5011
# {
#     'Price': 4.25
# }

# DELETE /books/5003
# Body: {'name':''jdsjdss}

@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    i=0
    for book in books:
        if book["isbn"] ==isbn:
            books.pop(i)
            response = Response("", status=204)
            return  response
        i += 1
    invalidBookObjectErrorMsg = {
        "error":"Book with the ISBN number that was provided was not found so therefore unable to delete"
    }
    response = Response(json.dumps(invalidBookObjectErrorMsg), status=404, mimetype='applcation/json')
    return response

@app.route('/')
def hello_world():
    return 'Hello World!'