# swap the dictionary key with its value

squares = {"a": 1, "b": 9, "c": 25, "d": 49, "t": 81}
my_dict = {}
for i in squares:
    val = squares[i]
    my_dict[val] = i
print(my_dict)  # {1: 'a', 9: 'b', 25: 'c', 49: 'd', 81: 't'}

dict1 = {"a":1,"d":6, "e":6,"b":3, "c":5, "y":45, "z":45}

print(dict1.items()) #dict_items([('a', 1), ('d', 6), ('e', 6), ('b', 3), ('c', 5), ('y', 45), ('z', 45)])
print(min(dict1.values())) # 1
print(max(dict1.values())) # 45

print(sorted(dict1.keys())) # ['a', 'b', 'c', 'd', 'e', 'y', 'z']
print(sorted(dict1.values())) # [1, 3, 5, 6, 6, 45, 45]

sortedkeys = sorted(dict1.keys())
sortedvalues = sorted(dict1.values())

print("min dict", {sortedkeys[0] :sortedvalues[0]}) # min dict {'a': 1}
print("max dict", {sortedkeys[-1] :sortedvalues[-1]}) #max dict {'z': 45}

print(dict(zip(sortedkeys, sortedvalues))) #{'a': 1, 'b': 3, 'c': 5, 'd': 6, 'e': 6, 'y': 45, 'z': 45}

print(sortedkeys[sortedvalues.index(45)]) # y

from collections import OrderedDict
print(OrderedDict({"a":1,"d":6, "e":6,"b":3, "c":5})) # OrderedDict([('a', 1), ('d', 6), ('e', 6), ('b', 3), ('c', 5)])