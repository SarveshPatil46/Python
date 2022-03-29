# NAME: SARVESH PATIL
# ROLL NO: 46

# Program to filter out only the even items from a list
list_example1 = [1, 5, 4, 6, 8, 11, 3, 12]

list_new1 = list(filter(lambda x: (x % 2 == 0), list_example1))

print(list_new1)

# Program to double each item in a list using map()

list_example2 = [1, 5, 4, 6, 8, 11, 3, 12]

list_new2 = list(map(lambda x: x * 2, list_example2))

print(list_new2)
