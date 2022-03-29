# NAME : SARVESH PATIL
# ROLL NO : 46

list_example = ['CNN', 'OS', 'EM4', 'AT', 'COA', 'PY']
print(list_example)

# first item
print(list_example[0])

# last item
print(list_example[-1])

list_example.append('PYTHON MINI PROJECT')
print(list_example)

list_example.remove('COA')
print(list_example)

print(list_example.count('OS'))

list_example.insert(2, 'New Subject')
print(list_example)

print(list_example.index('PY'))

list_example.sort()
print(list_example)

list_example.reverse()
print(list_example)

sub_copy = list_example.copy()
print(sub_copy)

list_example.clear()
print(list_example)
