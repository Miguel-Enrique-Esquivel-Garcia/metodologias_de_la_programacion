# Manejo de números y booleanos en Python
## Metodología de la Programación
#### Profesor: Charly Mercury, alias M.C. Carlos Antonio Tovar García
#### Alumno: Miguel Enrique Esquivel García
## Matrícula: 2530031
## Grupo: 1-1 IM

# Resumen Ejecutivo:
""" 
Los tipos int y float en Python representan números: int para valores enteros y float para decimales.  
La diferencia principal es que los int manejan cantidades discretas, mientras que los float permiten mayor precisión.  
Un booleano es un tipo lógico que solo puede ser True o False, y se obtiene mediante comparaciones.  
Validar rangos es esencial para asegurar que los datos sean coherentes y evitar errores en cálculos.  
También es crítico prevenir divisiones entre cero, ya que generan fallos en la ejecución del programa.  
El documento cubrirá la descripción de cada problema planteado y su contexto.  
Se detallará el diseño de entradas y salidas para garantizar claridad en los procesos.  
Se explicarán las validaciones aplicadas para mantener la robustez del sistema.  
Finalmente, se mostrará cómo los enteros, flotantes y booleanos se combinan para tomar decisiones lógicas.  
Todo esto permitirá comprender cómo se aplican estos conceptos en escenarios prácticos como nómina, descuentos o préstamos.  
"""
## Principios y Buenas Prácticas:
"""
- Usar tipos apropiados: int para contadores, float para cantidades con decimales.
- Evitar duplicar expresiones complejas: guardar resultados intermedios en variables.
- Validar datos antes de operar (por ejemplo, que horas y salarios no sean negativos).
- Usar nombres de variables descriptivos y mensajes claros para el usuario.
- Documentar claramente cómo se interpretan los booleanos (qué significa true y qué significa false en cada contexto).
"""
# Problemas
## Problem 1: Temperature converter and range flag
### Description:
"""
Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin. Además, determina un valor booleano 
is_high_temperature que sea true si la temperatura en Celsius es mayor o igual que 30.0 y false en caso contrario.
"""
### Inputs:
"""
- temp_c (float; temperatura en °C).
"""
### Outputs:
"""
- "Fahrenheit:" <temp_f>
- "Kelvin:" <temp_k>
- "High temperature:" true|false
"""
### Validations:
"""
- Verificar que temp_c pueda convertirse a float.
- No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).
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
Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a hourly_rate (float). 
Las horas extra (> 40) se pagan al 150% de la tarifa normal. Además, genera un booleano 
has_overtime que indique si el trabajador hizo horas extra.
"""
### Inputs:
"""
- hours_worked (float; horas trabajadas en la semana).
- hourly_rate (float; pago por hora).
"""
### Outputs:
"""
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false
"""
### Validations:
"""
- hours_worked >= 0
- hourly_rate > 0
- Si alguno no cumple, mostrar "Error: invalid input".
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
Determina si un cliente obtiene un descuento en su compra. La regla es:
- Tiene descuento si:
  - is_student es true OR
  - is_senior es true OR
  - purchase_total >= 1000.0
Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.
"""
### Inputs:
"""
- purchase_total (float; total de la compra).
- is_student_text (string; "YES" o "NO").
- is_senior_text (string; "YES" o "NO").
"""
### Outputs:
"""
- "Discount eligible:" true|false
- "Final total:" <final_total>
"""
### Validations:
"""
- purchase_total >= 0.0
- Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, is_senior.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".
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
Lee tres números enteros y calcula: suma, promedio (float), valor máximo, 
valor mínimo y un booleano all_even que indique si los tres números son pares.
"""
### Inputs:
"""
- n1 (int)
- n2 (int)
- n3 (int)
"""
### Outputs:
"""
- "Sum:" <sum_value>
- "Average:" <average_value>
- "Max:" <max_value>
- "Min:" <min_value>
- "All even:" true|false
"""
### Validations:
"""
- Verificar que los tres valores se puedan convertir a int.
- No se requieren restricciones adicionales (se permiten negativos).
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
Determina si una persona es elegible para un préstamo con base en:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
La regla es:
- debt_ratio = monthly_debt / monthly_income
- eligible es true si:
  - monthly_income >= 8000.0 AND
  - debt_ratio <= 0.4 AND
  - credit_score >= 650
"""
### Inputs:
"""
- monthly_income (float; ingreso mensual).
- monthly_debt (float; pagos mensuales de deuda).
- credit_score (int; puntaje de crédito).
"""
### Outputs:
"""
- "Debt ratio:" <debt_ratio>
- "Eligible:" true|false
"""
### Validations:
"""
- monthly_income > 0.0 (evitar división entre cero).
- monthly_debt >= 0.0
- credit_score >= 0
- Si no se cumple, mostrar "Error: invalid input".
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
Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
- bmi = weight_kg / (height_m * height_m)
Además, genera booleanos para indicar:
- is_underweight (bmi < 18.5)
- is_normal (18.5 <= bmi < 25.0)
- is_overweight (bmi >= 25.0)
"""
### Inputs:
"""
- weight_kg (float; peso en kilogramos).
- height_m (float; estatura en metros).
"""
### Outputs:
"""
- "BMI:" <bmi_redondeado>
- "Underweight:" true|false
- "Normal:" true|false
- "Overweight:" true|false
"""
### Validations:
"""
- weight_kg > 0.0
- height_m > 0.0
- Si no se cumple, mostrar "Error: invalid input".
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
Los enteros y flotantes se complementan en cálculos reales, pues juntos permiten representar cantidades exactas y valores con decimales.  
Las comparaciones generan booleanos que son la base para tomar decisiones con estructuras if, dando lógica al programa.  
Validar rangos asegura que los datos sean coherentes y evita errores críticos como divisiones entre cero.  
El uso de and, or y not en condiciones combinadas enseña a diseñar reglas más complejas y precisas.  
Estos patrones se repiten en problemas cotidianos como nómina, descuentos o préstamos, donde se mezclan cálculos y decisiones.  
Así, la programación refleja situaciones reales y se convierte en una herramienta confiable para automatizar procesos.  
Aprender estas bases fortalece la capacidad de modelar problemas y anticipar errores en sistemas prácticos.

"""
# Referencias:
"""
Fernández, M. (s. f.-b). Función int() en Python. https://thedataschools.com/python/funciones/int-funcion.html
Min() y max() de Python: encontrar valores más pequeños y más grandes. (s. f.). https://es.python-3.com/?p=149
Markaran, A., Melnikov, E., & Sumich, A. (2024, 3 mayo). Variables numéricas. https://diveintopython.org/es/learn/variables/number
Operadores lógicos. (s. f.). El Libro de Python. https://ellibrodepython.com/operadores-logicos
Python, R. (2014, 9 noviembre). Lógica en Python - Tipo Booleano - Recursos Python. Recursos Python. https://recursospython.com/guias-y-manuales/logica-tipo-booleano/
"""