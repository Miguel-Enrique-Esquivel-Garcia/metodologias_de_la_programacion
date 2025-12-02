#Borrador de pruebas
print("Problem 1: Palindrome checker (ignoring spaces and case)")
try:
    prase = input("Set a phrase: ").lower().strip().replace(" ","")

    print(prase)
    if prase == prase[::-1]:
        print("Is palindrome: true")
        print(prase[::-1])
    else:
        print("Is palindrome: false")
        print(prase[::-1])
except:
    print("Error: invalid input")

print("Problem 2 : Work hours and overtime payment")
try:
    hours_worked = float(input("Enter the number of hours worked in the week: "))
    hourly_rate = float(input("Enter the hourly wage: "))
    if hours_worked <= 40:
        total_payment = hours_worked * hourly_rate
    else:
        overtime_hours = hours_worked - 40
        total_payment = (40 * hourly_rate) + (overtime_hours * hourly_rate * 1.5)
    print(f"Total payment for the week: ${total_payment:.2f}")
except:
    print("Error: invalid input")

print("Problem 3: Student grades with dict and list")
grades ={"a": [100,100,100], "b":[90,98,70], "c": [20,78,100]}
sttudent_name = input("Enter the student's name (a, b, c): ").lower().strip()
if sttudent_name in grades:
    student_grades = grades[sttudent_name]
    average_grade = sum(student_grades) / len(student_grades)
    print(f"Grades for student {sttudent_name}: {student_grades}")
    print(f"Average grade: {average_grade:.2f}")
else:
    print("Error: student not found")
