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

if sentence == None or len(sentence) == 0:
    print("Error: invalid input")
else:
    

    print("Word count: ", len(sentence))
    print("First word: ", sentence[0])
    print("Last word: ", sentence[-1])
    
    longest_word = ""
    for word in sentence:
        if len(word) > len(longest_word):
            longest_word = word
    print("Longest word: ", longest_word)

    minword = len(longest_word)
    shortest_word = ""
    for word in sentence:
        if len(word) < minword:
            minword = len(word)
            shortest_word = word
    print("Shortest word: ", shortest_word)          

    


    
### Test cases.
""" 1) Normal:
Problem 4: Sentence word stats (lengths and first/last word)
Set a sentence: paulo le dijo a milo que lo quiere
Word count:  8
First word:  paulo
Last word:  quiere
Longest word:  quiere
Shortest word:  a
"""
""" 2) Border:
Problem 4: Sentence word stats (lengths and first/last word)
Set a sentence: y
Word count:  1
First word:  y
Last word:  y
Longest word:  y
Shortest word:
"""
""" 3) Error:
Problem 4: Sentence word stats (lengths and first/last word)
Set a sentence:
Error: invalid input
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
print("Problem 5: Password strength classifier")
password_input = input("Set your password: ")
password_input = password_input.strip()
if password_input == "":
    print("Error: invalid input")
else:
    if len(password_input) < 8 or (password_input.islower() == True or password_input.isupper() == True or password_input.isdigit() == True):
        print("Password strength: weak")
    elif len(password_input) >= 8 and password_input.isalnum() == True and ((any(char.isupper() for char in password_input) == True and any(char.islower() for char in password_input) == True)):
        print("Password strength: medium")
    elif len(password_input) >= 8 and password_input.isalnum() == False and any(char.isdigit() for char in password_input) == True and \
        any(char.islower() for char in password_input) == True and any(char.isupper() for char in password_input) == True:
        print("Password strength: strong")

    


### Test cases.
""" 1) Normal:
Problem 5: Password strength classifier
Set your password: AbC)3f9j¡K
Password strength: strong
"""
""" 2) Border:
Problem 5: Password strength classifier
Set your password: a
Password strength: weak
"""
""" 3) Error:
Problem 5: Password strength classifier
Set your password:
Error: invalid input
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
print("Problem 6: Product label formatter (fixed-width text)")
product_name = input("Set product name: ")
price_value = input("Set product price: ")
product_name = product_name.strip()

if product_name == "" or price_value == "" or float(price_value) <= 0:
    print("Error: invalid inputs")
else:
    label = f"Product: {product_name} | Price: ${price_value}"
    print(label)
    if len(label) == 30:
        print("`Label: ", label ,"'")
    elif len(label) < 30:
        while len(label) < 30:
            label = label + " "
        print("`Label: ", label ,"'")
    elif len(label) > 30:
        label = label[:30]
        print("`Label: ", label ,"'")


### Test cases.
""" 1) Normal:
Problem 6: Product label formatter (fixed-width text)
Set product name: pouyo
Set product price: 34.56
Product: pouyo | Price: $34.56
`Label:  Product: pouyo | Price: $34.56 '
"""
""" 2) Border:
Problem 6: Product label formatter (fixed-width text)
Set product name: a
Set product price: 1
Product: a | Price: $1
`Label:  Product: a | Price: $1         '
"""
""" 3) Error:
Problem 6: Product label formatter (fixed-width text)
Set product name:
Set product price:
Error: invalid inputs
"""


# Conclusiones:
""" 
"""
# Referencias:
"""
C, B. P. (2024, 17 mayo). Función len() de Python: Sintaxis, ejemplos y casos de uso. Geekflare Spain. https://geekflare.com/es/python-len-function/
Fernández, M. (s. f.). Método isdigit() en Python. https://thedataschools.com/python/strings/isdigit-metodo-string.html
GeeksforGeeks. (2025b, julio 15). Python Test if String contains any Uppercase character. GeeksforGeeks. https://www.geeksforgeeks.org/python/python-test-if-string-contains-any-uppercase-character/
GeeksforGeeks. (2025, 12 julio). Python Reverse Slicing of given string. GeeksforGeeks. https://www.geeksforgeeks.org/python/python-reverse-slicing-of-given-string/
Llamas, L. (2024, 20 noviembre). Qué son y cómo usar Slices en Python. Luis Llamas. https://www.luisllamas.es/python-slices/
W3Schools.com. (s. f.). https://www.w3schools.com/python/ref_list_count.asp
W3Schools.com. (s. f.-b). https://www.w3schools.com/python/ref_string_find.asp
"""