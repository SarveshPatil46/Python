# NAME : SARVESH PATIL
# ROLL NO : 46

string_example = 'Sarvesh Patil'
print(string_example)

# first character
print('string_example[0] = ', string_example[0])

# last character
print('string_example[-1] = ', string_example[-1])

# slicing 2nd to 5th character
print('string_example[1:5] = ', string_example[1:5])

upper = string_example.upper()
print(upper.isupper())

lower = string_example.lower()
print(lower.islower())

print(string_example.count('l'))

print(string_example.find('Patil'))

print(string_example.index('e'))

print(string_example.isnumeric())

print(string_example.split())

print(string_example.swapcase())

# character count
print('len(str) = ', len(string_example))

# Python string format() method
# default(implicit) order
default_order = "{}, {} and {}".format('Sarvesh', 'Samir', 'Patil')
print('\n--- Default Order ---')
print(default_order)
# order using positional argument
positional_order = "{1}, {0} and {2}".format('Sarvesh', 'Samir', 'Patil')
print('\n--- Positional Order ---')
print(positional_order)
# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='Sarvesh', b='Samir', s='Patil')
print('\n--- Keyword Order ---')
print(keyword_order)
