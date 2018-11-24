def validBookObj(bookObject):
    if ("name" in bookObject
            and "price" in bookObject
                and "isbn" in bookObject):
        return True
    else:
        return  False

valid_object = {
    'name':'F',
    'price': 6.00,
    'isbn': 3001
}

missing_name = {
    'price': 6.00,
    'isbn': 3001
}

missing_price = {
    'name':'F',
    'isbn': 3001
}

missing_isbn = {
    'name':'F',
    'price': 6.00,
}

empty_dictionary = {}