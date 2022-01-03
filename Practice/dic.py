customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}

print (customer["name"])
print (customer.get('name'))



phone = input("Phone: ")

digits_mappings = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
}
output = ''
for digit in phone:
    output += digits_mappings.get(digit, '!') + ' '
print(output)