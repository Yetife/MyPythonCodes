class Person:
    def __init__(self, name):
          self.name = name
    
    def talk(self):
        print(f'Hi, I am {self.name}')      

person1 = Person('John')
print(person1.name)
person1.talk()

person2 = Person('Boluwatife')
person2.talk()    