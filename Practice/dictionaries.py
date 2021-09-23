def create_a_student(first_name, last_name, email, phone_number, sex, courses=[]):
    student = {}
    student['first_name'] = first_name
    student['last_name'] = last_name
    student['email'] = email
    student['phone_number'] = phone_number
    student['sex'] = sex
    student['courses'] = []
   
    return student

class Native:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    
    def update_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
