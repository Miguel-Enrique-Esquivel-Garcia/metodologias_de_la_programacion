"""
Docstring del módulo understanding_while_cond.py
Vamos a hacer un programa
que describa un pin correcto,
definamos un máximo de intentos
y el usuario tiene que ingresar el pin correcto

Si el pin es correcto, mostramos un mensaje de bienvenida
Si el pin es incorrecto, mostraremos un mensaje de error

Si el usuario supera el máximo de intentos, muestra un mensaje de bloqueo
"""
MAX_ATTEMPTS = 3
CORRECT_PIN = "qwerty123"
attempts = 0

while attempts < MAX_ATTEMPTS:
    pin_entered = input("Set the secret pin: ")
    if pin_entered == CORRECT_PIN:
        print("Welcome my lord")
        break
    else:
        print("Try again")
        attempts += 1
if attempts == MAX_ATTEMPTS and pin_entered != CORRECT_PIN:
    print("Your account is locked")
    print("Goodbye")

print("masocomoelprofelohizo")
MAX_ATTEMPTS = 3
CORRECT_PIN = "qwerty123"
attempts = 0

while attempts < MAX_ATTEMPTS:
    pin_entered = input("Set the secret pin: ")
    if pin_entered == CORRECT_PIN:
        print("Welcome my lord")
        break
    else:
        attempts += 1
        remaining_attempst = MAX_ATTEMPTS - attempts
        if remaining_attempst > 0:
            print(f"Try again, you have {remaining_attempst} attempts left")
        else:
            print("No attempts left. Yousr account is locked")
