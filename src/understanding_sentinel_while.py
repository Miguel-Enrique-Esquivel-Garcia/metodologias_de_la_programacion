# While con centinela
"""
    Sumar n números hasta que el usuario escriba la palabra exit.
    También vamos a decir cuantos números ingrese el usuario.
    Cuál es el mínimo y cuál es el máximo.
"""
"""
Vamos a realizar un ejemplo que realice la suma de n números ingresados por el usuario,
no sabemos cuántos números se ingresan, quiere contablilizar cuántos números se han ingresado,
mostrar la suma, el mínimo y el máximo de los números ingresados.
"""
print("\n Captura de importes. Bienvenidos a la calculadora de importes(MXN). \n")
print("Para salir en cualquier momento escribe 'exit' \n")
counter = 0
sum_values = 0.0
maximum = None
minimum = None

while True:

    user_input = input("ingresa una cantidad: ")
    if user_input == "exit":
        break

    try:
        quantity = float(user_input)
    except:
        print("Ingresa un valor válido")
        continue

    counter += 1 # counter = counter + 1 (Contador de números ingresados)
    sum_values += quantity # sum = sum + quantity (Suma de los números ingresados)

    if minimum is None or quantity < minimum:
        minimum = quantity
    if maximum is None or quantity > maximum:
        maximum = quantity
print(sum_values)
print(counter)
print(maximum)
print(minimum)