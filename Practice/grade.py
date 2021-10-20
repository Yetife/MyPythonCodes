grade_score = int(input("Enter any number to input grade or -1 to cancel"))

score = []
while grade_score != -1:
    grade = int(input("Enter grade "))
    if grade >= 70 and grade <= 100:
        grade = "A" 
        print(grade)
        score.append(grade)
    elif grade >= 50 and grade <= 69:
        grade = "B"
        print(grade)
        score.append(grade)
    elif grade >= 40 and grade <= 49:
        grade = "C"
        print(grade)
        score.append(grade)
    elif grade >= 30 and grade <= 39:
        grade = "D"
        print(grade)
        score.append(grade)
    elif grade >= 20 and grade <= 29:
        grade = "E"
        print(grade)
        score.append(grade)
    elif grade >= 0 and grade <= 19:
        grade = "F"
        print(grade)
        score.append(grade)
    else:
        break
print(score)