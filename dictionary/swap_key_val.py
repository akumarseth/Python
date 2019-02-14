# swap the dictionary key with its value

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
my_dict = {}
for i in squares:
    val = squares[i]
    my_dict[val] = i
print(my_dict)