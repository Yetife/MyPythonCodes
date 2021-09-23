import dictionaries

cohort_eight_native = []

if __name__=='__main__':
    native = dictionaries.Native("Janet", "Doe")
    # print(native.first_name, native.last_name)
    print(native)
    native.update_name("Jackie", "Chan")
    print(native)
    native2 = dictionaries.Native("Tife", "Kim")
    print(native2)
    cohort_eight_native = [native.__str__(), native2.__str__()]
    print(cohort_eight_native)
    # student_1 = dictionaries.create_a_student('John', 'Doe', 'John_doe@gmail.com', '08095467219', 'male', 'courses=[]')
    # cohort_eight_native.append(student_1)
    # student_2 = dictionaries.create_a_student('Johanna', 'Doe', 'Johanna_doe@gmail.com', '08095467219', 'female', 'courses=[]')
    # cohort_eight_native.append(student_2)
    # student_3 = dictionaries.create_a_student('Johnny', 'Doe', 'Johnny_doe@gmail.com', '08095467219', 'male', 'courses=[]')
    # cohort_eight_native.append(student_3)
    # student_4 = dictionaries.create_a_student('Johnson', 'Doe', 'Johnson_doe@gmail.com', '08095467219', 'female', 'courses=[]')
    # cohort_eight_native.append(student_4)
    
    
    # student_1['courses'].append("java")
    # print(student_1)
    
    
    # for element in cohort_eight_native:
    #     if "java" in element['courses']:
    #         element['courses'].append("java")
    # print(cohort_eight_native)
    
    