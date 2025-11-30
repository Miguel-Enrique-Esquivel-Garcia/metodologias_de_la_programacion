# Manejo de strings en Python
## Metodología de la Programación
#### Profesor: Charly Mercury, alias M.C. Carlos Antonio Tovar García
#### Alumno: Miguel Enrique Esquivel García
## Matrícula: 2530031
## Grupo: 1-1 IM

# Resumen Ejecutivo:
""" 
Un string en Python es una secuencia inmutable de caracteres utilizada para almacenar y manipular texto.
Los strings se definen encerrando texto entre comillas simples (' '), dobles (" ") o triples (''' ''' o """ """).
Se pueden manipular mediante métodos incorporados como .upper(), .lower(), .strip(), .replace(), entre otros.
Las operaciones comunes incluyen concatenación (+), repetición (*), indexación (acceso a caracteres individuales) y slicing (subcadenas).
Las validaciones típicas incluyen verificar la longitud con len(), comprobar si un string está vacío, o si contiene ciertos caracteres o patrones.
También es importante validar y normalizar el texto de entrada (correos, nombres, contraseñas) para evitar errores, mantener coherenciay mejorar la seguridad.
Este documento cubrirá: descripción de cada problema, diseño de entradas y salidas, validaciones realizadas y uso de métodos 
de string, además de que se incluirán casos de prueba y el código correspondiente a cada problema.
"""
## Principios y Buenas Prácticas:
"""
- Los strings son inmutables: cualquier cambio genera una nueva cadena.
- Es buena práctica normalizar entrada con strip() y lower() antes de compararla.
- Evitar "números mágicos" en índices; documentar qué extrae cada slice.
- Usar métodos de string en lugar de reescribir lógica básica.
- Diseñar validaciones claras: primero que no esté vacío, luego el formato.
- Escribir código legible: nombres de variables claros y mensajes de error entendibles.
"""
# Problemas
## Problem 1: Full name formatter (name + initials)
### Description:
"""
Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).
"""
### Inputs:
"""
- full_name (string; nombre completo, puede venir en mayúsculas, minúsculas o mezclado, con espacios extra).
"""
### Outputs:
"""
- "Formatted name: <Name In Title Case>"
- "Initials: <X.X.X.>"
"""
### Validations:
"""
- El nombre completo debe contener entre 2 y 5 palabras.
- full_name no debe estar vacío después de strip().
- No aceptar cadenas que sean solo espacios.
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
Valida si una dirección de correo tiene un formato básico correcto:
- Contiene exactamente un '@'.
- Después del '@' debe haber al menos un '.'.
- No contiene espacios en blanco.
Si el correo es válido, también muestra el dominio (la parte después de '@').
"""
### Inputs:
"""
- email_text (string).
"""
### Outputs:
"""
- "Valid email: true" o "Valid email: false"
- Si es válido: "Domain: <domain_part>"
"""
### Validations:
"""
- email_text no vacío tras strip().
- Contar cuántas veces aparece '@'.
- Verificar que no haya espacios (no debe haber " " en email_text).
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
Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha y de derecha a izquierda, 
ignorando espacios y mayúsculas/minúsculas.


Ejemplos:
- "Anita lava la tina" -> palíndromo.
- "Hola mundo" -> no palíndromo.
"""
### Inputs:
"""
- phrase (string).
"""
### Outputs:
"""
- "Is palindrome: true" o "Is palindrome: false"
- Mostrar también la versión normalizada de la frase.
"""
### Validations:
"""
- phrase no vacía tras strip().
- Longitud mínima razonable después de limpiar espacios (por ejemplo, al menos 3 caracteres).
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
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   - Primera palabra.
   - Última palabra.
   - Palabra más corta y más larga (por longitud).
"""
### Inputs:
"""
- sentence (string).
"""
### Outputs:
"""
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"
"""
### Validations:
"""
- Oración no vacía tras strip().
- Debe contener al menos una palabra válida después de split().
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
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas (puedes afinarlas, pero documéntalas en los comentarios).

Ejemplo de reglas:
- Weak: longitud < 8 o todo en minúsculas o muy simple.
- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).
"""
### Inputs:
"""
- password_input (string).
"""
### Outputs:
"""
- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"
"""
### Validations:
"""
- No aceptar contraseña vacía.
- Verificar longitud con len().
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
Dado el nombre de un producto y su precio, 
genera una etiqueta en una sola línea con el siguiente formato:

Product: <NAME> | Price: $<PRICE>

La cadena completa debe tener exactamente 30 caracteres:
- Si es más corta, rellena con espacios al final.
- Si es más larga, recorta hasta 30 caracteres.
"""
### Inputs:
"""
-product_name (string).
- price_value (string).
"""
### Outputs:
"""
- "Label: <exactly 30 characters>" (la etiqueta entre comillas para que se vean los espacios.)
"""
### Validations:
"""
- product_name no vacío tras strip().
- price_value debe poder convertirse a un número positivo.
"""
print("Problem 6: Product label formatter (fixed-width text)")
product_name = input("Set product name: ")
price_value = input("Set product price: ")
product_name = product_name.strip()

if product_name == "" or price_value == "" or float(price_value) <= 0:
    print("Error: invalid inputs")
else:
    label = f"Product: {product_name} | Price: ${price_value}"
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
`Label:  Product: pouyo | Price: $34.56 '
"""
""" 2) Border:
Problem 6: Product label formatter (fixed-width text)
Set product name: a
Set product price: 1
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
Los strings en Python son herramientas poderosas para manejar y manipular texto.
A través de este conjunto de problemas, hemos explorado diversas técnicas para normalizar, validar y formatear cadenas de texto.
Hemos aprendido la importancia de las validaciones para asegurar la integridad de los datos y evitar errores comunes.
Al utilizar métodos incorporados de strings, podemos simplificar nuestras tareas y mejorar la legibilidad del código.
Además, la práctica constante con problemas reales nos ayuda a consolidar nuestro entendimiento y habilidades en el manejo de strings en Python.
Su inmutabilidad y la variedad de métodos disponibles hacen que trabajar con strings sea eficiente y efectivo en el desarrollo de aplicaciones.
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