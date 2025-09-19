biggest_score= 0
smallest_score = 0
average_score = 0
number_of_students= 0
good_students= ['ali','reza']
bad_students= ['peyman']
while number_of_students < 10:
    names_of_students=(input("Enter your name: ")).lower()
    students_grades=float(input("Enter your grade: "))
    if students_grades < 0 or students_grades > 20: #to get the correct score
        print("Please enter a number between 0 and 20")
        continue
    