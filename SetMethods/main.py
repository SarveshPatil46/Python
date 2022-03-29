# NAME : SARVESH PATIL
# ROLL NO : 46

set_example = {'Sarvesh Patil', '46', 'D10A'}
print(set_example)

set_example.add('VESIT')
print(set_example)

set_example.update(['Mumbai', 'Sarvesh Patil', 'India'])
print(set_example)

set_example.remove('Mumbai')
print(set_example)

print('Sarvesh Patil' in set_example)

set_example.clear()
print(set_example)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union
print(A | B)

# Intersection
print(A & B)

# Difference
print(A - B)
