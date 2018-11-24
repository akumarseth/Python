from flask import Flask, jsonify, request,Response

from BookModel import *
from settings import *
import json

@app.route('/books')
def get_books():
    return jsonify({'books': Book().get_all_books()})

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
        Book.add_book(request_data['name'], request_data['price'], request_data['isbn'])
        response = Response("Success", 201, mimetype="application/jsom")
        response.headers['Location'] = "/books"+ str(request_data['isbn'])
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
    book_details = Book.get_book(isbn)
    return_obj = {
        'name': book_details.name,
        'price': book_details.price,
        'isbn': book_details.isbn
    }
    return jsonify(return_obj)

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

    Book.replace_book(request_data['name'], request_data['price'], request_data['isbn'])
    response = Response("", status=204)
    return response

@app.route('/books/<int:isbn>', methods=['PATCH'])
def update_book(isbn):
    request_data = request.get_json()
    if "name" in request_data:
        Book.update_book_name(isbn,request_data['name'])
    if "price" in request_data:
        Book.update_book_price(isbn, request_data['price'])
    response = Response("", 204, mimetype="application/jsom")
    response.headers['Location'] = "/books" + str(isbn)
    return response

@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    if(Book.delete_book(isbn)):
        response = Response("", status=204)
        return response
    invalidBookObjectErrorMsg = {
        "error":"Book with the ISBN number that was provided was not found so therefore unable to delete"
    }
    response = Response(json.dumps(invalidBookObjectErrorMsg), status=404, mimetype='applcation/json')
    return response

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)