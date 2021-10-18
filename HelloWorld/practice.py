student_name = 'Soyuj'

marks = {'James': 90, 'Soyuj': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')
    

#     iter('foobar')                             # String
# <str_iterator object at 0x036E2750>

# >>> iter(['foo', 'bar', 'baz'])                # List
# <list_iterator object at 0x036E27D0>

# >>> iter(('foo', 'bar', 'baz'))                # Tuple
# <tuple_iterator object at 0x036E27F0>

# >>> iter({'foo', 'bar', 'baz'})                # Set
# <set_iterator object at 0x036DEA08>

# >>> iter({'foo': 1, 'bar': 2, 'baz': 3})       # Dict
# <dict_keyiterator object at 0x036DD990>
# dictionary has keys and values