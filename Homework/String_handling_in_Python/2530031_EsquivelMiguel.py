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

print("Problem 1: Full name formatter (name + initials)")
fullname = input("Set your full name: ")
if len(fullname.split()) <2 or len(fullname.split()) >5:
    print("Error: invalid input") 
else:
    fullname = fullname.split()
    if len(fullname) == 5:
        fullname = fullname[-5] + " " + fullname[-4] + " " + fullname[-3] + " " + fullname[-2] + " " + fullname[-1]
        fullname = fullname.strip()
        print("Formatted Name: ", fullname.title())
    elif len(fullname) == 4:
        fullname = fullname[-4] + " " + fullname[-3] + " " + fullname[-2] + " " + fullname[-1]
        fullname = fullname.strip()
        print("Formatted Name: ", fullname.title())
    elif len(fullname) == 3:
        fullname = fullname[-3] + " " + fullname[-2] + " " + fullname[-1]
        fullname = fullname.strip()
        print("Formatted Name: ", fullname.title())
    elif len(fullname) == 2:
        fullname = fullname[-2] + " " + fullname[-1]
        fullname = fullname.strip()
        print("Formatted Name: ", fullname.title())
    
    initials = fullname.split()
    if len(initials) == 5:
        initials = (initials[-5][0] + "." + initials[-4][0] + "." + initials[-3][0] + "." + initials[-2][0] + "." + initials[-1][0] + ".").upper()
        print("Initials: ", initials)
    elif len(initials) == 4:
        initials = (initials[-4][0] + "." + initials[-3][0] + "." + initials[-2][0] + "." + initials[-1][0] + ".").upper()
        print("Initials: ", initials)
    elif len(initials) == 3:
        initials = (initials[-3][0] + "." + initials[-2][0] + "." + initials[-1][0] + ".").upper()
        print("Initials: ", initials)
    elif len(initials) == 2:
        initials = (initials[-2][0] + "." + initials[-1][0] + ".").upper()
        print("Initials: ", initials)

### Test cases.
""" 1) Normal:
Problem 1: Full name formatter (name + initials)
Set your full name:  migUel   EnriqUE esquivel garCÍa
Formatted Name:  Miguel Enrique Esquivel García
Initials:  M.E.E.G.
"""
""" 2) Border:
Problem 1: Full name formatter (name + initials)
Set your full name: WEBI wabo
Formatted Name:  Webi Wabo
Initials:  W.W.
"""
""" 3) Error:
Problem 1: Full name formatter (name + initials)
Set your full name:
Error: invalid input
"""


## Problem 2: Simple email validator (structure + domain)
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

print("Problem 2: Simple email validator (structure + domain)")
email_text = input("Set your email address: ")
email_text = email_text.strip()
if email_text.count("@") == 1:
    email_parts = email_text.split("@")
    if len(email_parts[-2]) > 0 and len(email_parts[-1]) >= 3:
        if (email_parts[-1]).count(".") >= 1:
            at = email_text.find("@")
            dot = (email_parts[-1]).find(".")
            if at > 0 and dot > 0 and dot < len(email_parts[-1]) - 1:
                print("Valid email: true")
                print("Domain:", email_parts[-1])
            else:
                print("Valid email: false")
        else:
            print("Valid email: false")
    else:
        print("Valid email: false")
else:
    print("Valid email: false")


### Test cases.
""" 1) Normal:
Problem 2: Simple email validator (structure + domain)
Set your email address: wisdommasterjr@gmail.com
Valid email: true
Domain: gmail.com
"""
""" 2) Border:
Problem 2: Simple email validator (structure + domain)
Set your email address: papu@v.v
Valid email: true
Domain: v.v
"""
""" 3) Error:
Problem 2: Simple email validator (structure + domain)
Set your email address:
Valid email: false
"""

## Problem 3: Palindrome checker (ignoring spaces and case)
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

print("Problem 3: Palindrome checker (ignoring spaces and case)")
phrase = input("Set a palindrome phrase: ")
phrase = phrase.replace(" ","").lower().strip()
print("Processed phrase: ", phrase)
if phrase == phrase[::-1] and len(phrase) >=3:
    print("Is palindrome: true")
    print("Reversed phrase: ", phrase[::-1])
else:
    print("Is palindrome: false")
    print("Reversed phrase: ", phrase[::-1])

### Test cases.
""" 1) Normal:
Problem 3: Palindrome checker (ignoring spaces and case)
Set a palindrome phrase: Amo La Pacifica Paloma
Processed phrase:  amolapacificapaloma
Is palindrome: true
Reversed phrase:  amolapacificapaloma
"""
""" 2) Border:
Problem 3: Palindrome checker (ignoring spaces and case)
Set a palindrome phrase: OSo
Processed phrase:  oso
Is palindrome: true
Reversed phrase:  oso
"""
""" 3) Error:
Problem 3: Palindrome checker (ignoring spaces and case)
Set a palindrome phrase:
Processed phrase:
Is palindrome: false
Reversed phrase:
"""

## Problem 4: Sentence word stats (lengths and first/last word)
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

print("Problem 4: Sentence word stats (lengths and first/last word)")
sentence = input("Set a sentence: ")
sentence = sentence.strip()
sentence = sentence.split()

if sentence == "":
    print("Error: invalid input")
else:
    print("Word count: ", len(sentence))
    print("First word: ", sentence[0])
    print("Last word: ", sentence[-1])
    



    
### Test cases.
""" 1) Normal:

"""
""" 2) Border:

"""
""" 3) Error:

"""

## Problem 5: Password strength classifier
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

## Problem 6: Product label formatter (fixed-width text)
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
C, B. P. (2024, 17 mayo). Función len() de Python: Sintaxis, ejemplos y casos de uso. Geekflare Spain. https://geekflare.com/es/python-len-function/
GeeksforGeeks. (2025, 12 julio). Python Reverse Slicing of given string. GeeksforGeeks. https://www.geeksforgeeks.org/python/python-reverse-slicing-of-given-string/
W3Schools.com. (s. f.). https://www.w3schools.com/python/ref_list_count.asp
W3Schools.com. (s. f.-b). https://www.w3schools.com/python/ref_string_find.asp
"""