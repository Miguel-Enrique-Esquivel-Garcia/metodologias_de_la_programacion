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



### Test cases.
""" 1) Normal:

"""
""" 2) Border:

"""
""" 3) Error:

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



### Test cases.
""" 1) Normal:

"""
""" 2) Border:

"""
""" 3) Error:

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



### Test cases.
""" 1) Normal:

"""
""" 2) Border:

"""
""" 3) Error:

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



### Test cases.
""" 1) Normal:

"""
""" 2) Border:

"""
""" 3) Error:

"""


# Conclusiones:
""" 
"""
# Referencias:
"""
"""