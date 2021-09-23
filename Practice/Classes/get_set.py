class Student(object):
    def __init__(self, name):
        self.name = name

student = Student(' Olasehinde Yetunde')
print (student.name)
student.name = "Python"
print (student.name)    