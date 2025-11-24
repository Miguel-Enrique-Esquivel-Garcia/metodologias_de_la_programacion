# Manejo de strings en Python
## Metodología de la Programación
#### Profesor: Charly Mercury, alias M.C. Carlos Antonio Tovar García
#### Alumno: Miguel Enrique Esquivel García
## Matrícula: 2530031
## Grupo: 1-1 IM

# Resumen Ejecutivo:
""" 
"""
# Problemas
## Problem 1: Full name formatter (name + initials)
fullname = input("Set your full name: ")
if len(fullname.split()) <=3 or len(fullname.split()) >=5:
    print("Error: invalid input") 
else:
    fullname = fullname.strip()
    print("Formatted Name: ", fullname.title())
    
    initials = fullname.split()
    if len(initials) == 5:
        initials = (initials[-5][0] + initials[-4][0] + initials[-3][0] + initials[-2][0] + initials[-1][0]).upper()
        print("Initials: ", initials)
    elif len(initials) == 4:
        initials = (initials[-4][0] + initials[-3][0] + initials[-2][0] + initials[-1][0]).upper()
        print("Initials: ", initials)
    elif len(initials) == 3:
        initials = (initials[-3][0] + initials[-2][0] + initials[-1][0]).upper()
        print("Initials: ", initials)


## Problem 2: 
## Problem 3: 
## Problem 4: 
## Problem 5: 
## Problem 6: 

# Conclusiones:
""" 
"""
# Referencias:
"""
"""