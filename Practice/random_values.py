import random

for i in range(3):
    print(random.randint(10, 20))
     
# print(random.random())


members = ['Mary', "John", 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)
    