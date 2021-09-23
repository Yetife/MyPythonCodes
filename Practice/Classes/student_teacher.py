class Person(object):
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return self.name

class Student(Person):
    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        
    def get_details(self):
        return "%s studies %s is in %s year." % (self.name, self.branch, self.year)

class Teacher(Person):
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers
    
    def get_details(self):
        return "%s teaches %s " % (self.name, ','.join(self.papers))

person1 = Person('Yetunde')
student1 = Student('Olasehinde', 'Software Engineering', '2021')
teacher1 = Teacher('Tony', ['Java', 'Python'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())

person2 = Person('Segun')
student2 = Student('Olasehinde', 'Semicolon', '2021')
teacher2 = Teacher('Tony', ['Java', 'Python'])

print(person2.get_details())
print(student2.get_details())
print(teacher2.get_details())