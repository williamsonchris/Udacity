names = []
assignments = []
grades = []
all_student_data = ()

def user_inputs():
    for i in range (0,2):
        input_names = input("please enter the name of the student ")
        names.append(input_names)
        input_assignments = input('please enter assignments counts ')
        assignments.append(input_assignments)
        input_grades = input('please enter the students grades ')
        grades.append(input_grades)

        print(names)
        print(assignments)
        print(grades)

def send_emails():
    all_student_data = list(zip(names, assignments, grades))
    for i in all_student_data:
        print(all_student_data)
        print("hi {}, just wanted to give you a heads up. You currently have {} assignments outstanding and your current grade for the course is {}".format(i[0],i[1],i[2]))

user_inputs()
send_emails()
