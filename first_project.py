biggest_grade = 0
smallest_grade = 21
average_grade = 0
number_of_students = 1
good_students = ['ali','reza']
bad_students = ['peyman','eli']
while number_of_students < 10:
    names_of_students=(input("Enter your name: ")).lower()
    students_grades=float(input("Enter your grade: "))
    if students_grades < 0 or students_grades > 20: #to get the correct grade
        print("Please enter a number between 0 and 20")
        continue
    if names_of_students in good_students: #For disorganized and organized students
        students_grades += 2
        print('since you were a bit organized student, 2 points will be added to your grade')
        if students_grades > 18: #because if the grade is above 18, it will show a score bigger than 20.
            print('your name: ', names_of_students)
            print('your grade: 20')
            print('Great, you are accepted')
        elif students_grades >= 15 or students_grades <= 18:
            print('your name: ', names_of_students)
            print('your grade: ', students_grades)
            print('Great, you are accepted')
        elif students_grades >= 12 or students_grades < 15:
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
        if students_grades < 2: #because if the grade is below 2, it will show a score as negative zero.
            print('your name: ', names_of_students)
            print('your grade: 0')
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
average_grade = (average_grade / number_of_students) // 1
print("The average grade is " , average_grade) # grades results
print("The smallest grade is " , smallest_grade)
print("The biggest grade is " , biggest_grade)