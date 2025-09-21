biggest_grade = 0
blocked_people = []
invalid_input = 1
smallest_grade = 21
average_grade = 0
number_of_students = 0
good_students = ['ali','reza']
bad_students = ['peyman','eli']
while number_of_students < 10:
    names_of_students=(input("Enter your name: ")).lower()
    if names_of_students in blocked_people:
        print("your account is blocked you can't continue.")
        continue
    students_grades=float(input("Enter your grade: "))
    if students_grades < 0 or students_grades > 20: #to get the correct grade
        if invalid_input > 2: #So that if someone makes more than three mistakes, their account will be blocke
            print("your account is blocked")
            blocked_people = names_of_students
            continue
        print("Please enter a number between 0 and 20")
        invalid_input += 1
        continue
    if names_of_students in good_students: #For disorganized and organized students
        students_grades += 2
        print('since you were a bit organized student, 2 points will be added to your grade')
        if students_grades > 20: #because if the grade is above 18, it will show a score bigger than 20.
            students_grades = 20
            print('your name: ', names_of_students)
            print('your grade: ' , students_grades)
            print('Great, you are accepted')
        elif students_grades > 17 and students_grades < 21:
            print('your name: ', names_of_students)
            print('your grade: ', students_grades)
            print('Great, you are accepted')
        elif students_grades >= 15 and students_grades <= 18:
            print('your name: ', names_of_students)
            print('your grade: ', students_grades)
            print('well down! you passed the exam')
        elif students_grades >= 12 and students_grades < 15:
            print('your name: ', names_of_students)
            print('your grade: ', students_grades)
            print('you have passed, but try harder')
        else:
            print('your name: ', names_of_students)
            print('your grade: ', students_grades)
            print("Awful, You didn't pass")
    elif names_of_students in bad_students:
        students_grades -= 2
        print('Since you were a disorganized student, 2 points will be deducted from your grade')
        if students_grades < 0: #because if the grade is below 2, it will show a score as negative zero.
            students_grades = 0
            print('your name: ', names_of_students)
            print('your grade: 0')
            print("Awful, You didn't pass")
        elif students_grades >= 0 and students_grades < 3:
            print('your name: ', names_of_students)
            print('your grade: ', students_grades)
            print("Awful, You didn't pass")
        elif students_grades == 18:
            print('your name: ', names_of_students)
            print('your grade: ', students_grades)
            print('Great, you are accepted')
        elif students_grades >=15 and students_grades < 18:
            print('your name: ', names_of_students)
            print('your grade: ', students_grades)
            print('well down! you passed the exam')
        elif students_grades >=12 and students_grades < 15:
            print('your name: ', names_of_students)
            print('your grade: ', students_grades)
            print('you have passeelid, but try harder')
        else:
            print('your name: ', names_of_students)
            print('your grade: ', students_grades)
            print("Awful, You didn't pass")
    elif students_grades >= 18 and students_grades <= 20: #To check the students' grades
        print('your name: ' , names_of_students)
        print('your grade: ' , students_grades)
        print('Great, you are accepted')
    elif students_grades >= 15 and students_grades < 18:
        print('your name: ', names_of_students)
        print('your grade: ', students_grades)
        print('well down! you passed the exam')
    elif students_grades >= 12 and students_grades < 15:
        print('your name: ', names_of_students)
        print('your grade: ', students_grades)
        print('you have passed, but try harder')
    else:
        print('your name: ', names_of_students)
        print('your grade: ', students_grades)
        print("Awful, You didn't pass")
    average_grade += students_grades  # For the average grades
    if students_grades > biggest_grade:  # For the biggest grade and smallest grade
        biggest_grade = students_grades
    if students_grades < smallest_grade:
        smallest_grade = students_grades
    number_of_students += 1
    #print(average_grade , )
    #print(number_of_students)
average_grade = (average_grade / number_of_students) // 1
print("\nThe average grade is " , average_grade) # grades results
print("The smallest grade is " , smallest_grade)
print("The biggest grade is " , biggest_grade)