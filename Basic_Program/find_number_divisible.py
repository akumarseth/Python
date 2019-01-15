# Python Program to find numbers divisible by thirteen from a list using anonymous function

# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,225,30]

# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))
result1 = [x for x in my_list if x%15 == 0]
# display the result
print("Numbers divisible by 13 are",result)
print("Numbers divisibleby 15 are", result1)
