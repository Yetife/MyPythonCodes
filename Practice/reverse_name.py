# name = input("Enter a name: ")

# print(name.strip[-1:2])


for i in [1, 2, 3, 4, 5]:
    print ("printing i", i)
    for j in [1, 2, 3, 4, 5]:
        print ("printing j", j)
        print ("addition of i and j",i + j)
    print ("printing i", i)
print ("done looping")

import re
my_regex = re.compile("[0-9]+", re.I)