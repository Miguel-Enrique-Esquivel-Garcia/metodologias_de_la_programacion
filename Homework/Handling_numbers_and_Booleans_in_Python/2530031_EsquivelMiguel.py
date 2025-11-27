# Manejo de números y booleanos en Python
## Metodología de la Programación
#### Profesor: Charly Mercury, alias M.C. Carlos Antonio Tovar García
#### Alumno: Miguel Enrique Esquivel García
## Matrícula: 2530031
## Grupo: 1-1 IM

# Resumen Ejecutivo:
""" 
"""
## Principios y Buenas Prácticas:
"""

"""
# Problemas
## Problem 1: Temperature converter and range flag
### Description:
"""

"""
### Inputs:
"""

"""
### Outputs:
"""

"""
### Validations:
"""

"""

print("Problem 1: Temperature converter and range flag")
temp_c = input("Enter temperature in Celsius: ")
try:
    temp_c = float(temp_c)
    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15
    is_high_temperature = (temp_c >= 30.0)
    if temp_k < 0.0:
        print("Error: invalid input")
    else:
        if is_high_temperature == True:
            print("Farenheit: ", temp_f)
            print("Kelvin: ", temp_k)
            print("High temperature:", is_high_temperature)
        else:
            print("Farenheit: ", temp_f)
            print("Kelvin: ", temp_k)
            print("High temperature:", is_high_temperature)
except:
    print("Error: invalid input")



### Test cases.
""" 1) Normal:
Problem 1: Temperature converter and range flag
Enter temperature in Celsius: 30
Farenheit:  86.0
Kelvin:  303.15
High temperature: True
"""
""" 2) Border:
Problem 1: Temperature converter and range flag
Enter temperature in Celsius: -273.15
Farenheit:  -459.66999999999996
Kelvin:  0.0
High temperature: False
"""
""" 3) Error:
Problem 1: Temperature converter and range flag
Enter temperature in Celsius: -273.16
Error: invalid input
"""

## Problem 2: Work hours and overtime payment
### Description:
"""

"""
### Inputs:
"""

"""
### Outputs:
"""

"""
### Validations:
"""

"""

print("Problem 2: Work hours and overtime payment")
hours_worked = input("Hours worked at week: ")
hourly_rate = input("Pay per hour: ")

try:
    hours_worked = float(hours_worked)
    hourly_rate = float(hourly_rate)
    if hours_worked > 0 or hourly_rate >= 0:
        has_overtime = (hours_worked > 40)
        if has_overtime == True:
            regular_pay = 40 * hourly_rate
            overtime_hours = hours_worked - 40
            overtime_pay = overtime_hours * hourly_rate * 1.5
            total_pay = regular_pay + overtime_pay
            print("Regular pay: ", regular_pay)
            print("Overtime pay: ", overtime_pay)
            print("Total pay: ", total_pay)
            print("Has overtime: ",has_overtime)
        else:
            regular_pay = hours_worked * hourly_rate
            overtime_pay = 0.0
            overtime_pay = 0.0
            total_pay = regular_pay + overtime_pay
            print("Regular pay: ", regular_pay)
            print("Overtime pay: ", overtime_pay)
            print("Total pay: ", total_pay)
            print("Has overtime: ", has_overtime)

    else:
        print("Error: invalid values")
except:
    print("Error: invalid values")

### Test cases.
""" 1) Normal:
Problem 2: Work hours and overtime payment
Hours worked at week: 50
Pay per hour: 100.5
Regular pay:  4020.0
Overtime pay:  1507.5
Total pay:  5527.5
Has overtime:  True
"""
""" 2) Border:
Problem 2: Work hours and overtime payment
Hours worked at week: 1
Pay per hour: 0
Regular pay:  0.0
Overtime pay:  0.0
Total pay:  0.0
Has overtime:  False
"""
""" 3) Error:
Problem 2: Work hours and overtime payment
Hours worked at week: 0
Pay per hour: -10
Error: invalid values
"""

## Problem 3: Discount eligibility with booleans
### Description:
"""

"""
### Inputs:
"""

"""
### Outputs:
"""

"""
### Validations:
"""

"""

print("Problem 3: Discount eligibility with booleans")
try:
    purchase_total = float(input("Set the total of your purchase: "))
    is_student_text = str(input("Are you a student? (YES/NO): ")).upper()
    is_senior_text = str(input("Are you a senior? (YES/NO): ")).upper()
    if purchase_total >= 0 or is_student_text == "YES" and is_student_text == "NO" or is_senior_text == "YES" and is_senior_text == "NO":
        if is_student_text == "YES":
            is_student_text = True
        elif is_student_text == "NO":
            is_student_text = False
        if is_senior_text == "YES":
            is_senior_text = True
        elif is_senior_text == "NO":
            is_senior_text = False
        if is_student_text == True or is_senior_text == True or purchase_total >= 1000:
            discount_elegible = True
            final_total = purchase_total * 0.9
            print("Discount eligible: ", discount_elegible)
            print("Final total: ", final_total)
        else:
            discount_elegible = False
            final_total = purchase_total
            print("Discount eligible: ", discount_elegible)
            print("Final total: ", final_total)
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")


### Test cases.
""" 1) Normal:
Problem 3: Discount eligibility with booleans
Set the total of your purchase: 1000
Are you a student? (YES/NO): YES
Are you a senior? (YES/NO): NO
Discount eligible:  True
Final total:  900.0
"""
""" 2) Border:
Problem 3: Discount eligibility with booleans
Set the total of your purchase: 1
Are you a student? (YES/NO): No
Are you a senior? (YES/NO): yes
Discount eligible:  True
Final total:  0.9
"""
""" 3) Error:
Problem 3: Discount eligibility with booleans
Set the total of your purchase:
Error: invalid input
"""

## Problem 4: Basic statistics of three integers
### Description:
"""

"""
### Inputs:
"""

"""
### Outputs:
"""

"""
### Validations:
"""

"""

print("Problem 4: Basic statistics of three integers")

try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = int(input("Enter the third number: "))
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    min_value = min(n1, n2, n3)
    max_value = max(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    print("Sum: ", sum_value)
    print("Average: ", average_value)
    print("Max: ", max_value)
    print("Min: ", min_value)
    print("All even: ", all_even)
except:
    print("Error: invalid input")

### Test cases.
""" 1) Normal:
Problem 4: Basic statistics of three integers
Enter the first number: 2
Enter the second number: 6
Enter the third number: 14
Sum:  22
Average:  7.333333333333333
Max:  14
Min:  2
All even:  True
"""
""" 2) Border:
Problem 4: Basic statistics of three integers
Enter the first number: 9
Enter the second number: -70
Enter the third number: 4
Sum:  -57
Average:  -19.0
Max:  9
Min:  -70
All even:  False
"""
""" 3) Error:
Problem 4: Basic statistics of three integers
Enter the first number: f
Error: invalid input
"""

## Problem 5: Loan eligibility (income and debt ratio)
### Description:
"""

"""
### Inputs:
"""

"""
### Outputs:
"""

"""
### Validations:
"""

"""

print("Problem 5: Loan eligibility (income and debt ratio)")
try:
    monthly_income = float(input("Set your monthly income: "))
    monthly_debt = float(input("Set a monthly income: "))
    credit_score = int(input("Set your credit score: "))
    if monthly_income > 0.0 or monthly_debt >= 0.0 or credit_score >= 0:
        debt_ratio = monthly_debt / monthly_income
        if monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650:
            eligible = True
        else:
            eligible = False
        print("Debt ratio: ", debt_ratio)
        print("Eligible: ", eligible)
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")

### Test cases.
""" 1) Normal:
Problem 5: Loan eligibility (income and debt ratio)
Set your monthly income: 50000
Set a monthly income: 6
Set your credit score: 750
Debt ratio:  0.00012
Eligible:  True
"""
""" 2) Border:
Problem 5: Loan eligibility (income and debt ratio)
Set your monthly income: 0.1
Set a monthly income: 0
Set your credit score: 0
Debt ratio:  0.0
Eligible:  False
"""
""" 3) Error:
Problem 5: Loan eligibility (income and debt ratio)
Set your monthly income: 9000.67
Set a monthly income: d
Error: invalid input
"""

## Problem 6: Body Mass Index (BMI) and category flag
### Description:
"""

"""
### Inputs:
"""

"""
### Outputs:
"""

"""
### Validations:
"""

"""

print("Problem 6: Body Mass Index (BMI) and category flag")
try:
    weight_kg = float(input("Set your weight in kilograms: "))
    height_m = float(input("Set your height in meters: "))
    if weight_kg > 0 and height_m > 0.0:
        bmi = weight_kg / (height_m * height_m)
        if bmi < 18.5:
            is_underweight = True
            is_normal = False
            is_overweight = False
        elif 18.5 <= bmi < 25.0:
            is_underweight = False
            is_normal = True
            is_overweight = False
        elif bmi >= 25.0:
            is_underweight = False
            is_normal = False
            is_overweight = True
        bmi_redondeado = round(bmi, 2)
        print("BMI:", bmi_redondeado)
        print("Underweight:", is_underweight)
        print("Normal:", is_normal)
        print("Overweight:", is_overweight)
    else:
        print("Error: invalid input")
except:
    print("Error: invalid input")


### Test cases.
""" 1) Normal:
Problem 6: Body Mass Index (BMI) and category flag
Set your weight in kilograms: 48
Set your height in meters: 1.675
BMI: 17.11
Underweight: True
Normal: False
Overweight: False
"""
""" 2) Border:
Problem 6: Body Mass Index (BMI) and category flag
Set your weight in kilograms: 1
Set your height in meters: 0.1
BMI: 100.0
Underweight: False
Normal: False
Overweight: True
"""
""" 3) Error:
Problem 6: Body Mass Index (BMI) and category flag
Set your weight in kilograms: a
Error: invalid input
"""


# Conclusiones:
""" 
"""
# Referencias:
"""
Fernández, M. (s. f.-b). Función int() en Python. https://thedataschools.com/python/funciones/int-funcion.html
Min() y max() de Python: encontrar valores más pequeños y más grandes. (s. f.). https://es.python-3.com/?p=149

"""