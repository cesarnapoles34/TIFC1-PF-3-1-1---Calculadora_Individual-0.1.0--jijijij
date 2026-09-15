numero1 = float(input("Introduce el primer numero: "))
numero2 = float(input("Introduce el segundo numero: "))

resultado = numero1 + numero2
print(f"El resultado de la suma es: {resultado}")

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre 0"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Error: no se puede calcular el modulo entre 0"
    return a % b

def sumar_tres(a, b, c):
    return a + b + c

def operaciones_mixtas(numeros, operadores):
    resultado = numeros[0]
    for i, operador in enumerate(operadores):
        siguiente = numeros[i + 1]
        if operador == "+":
            resultado = resultado + siguiente
        elif operador == "-":
            resultado = resultado - siguiente
        elif operador == "*":
            resultado = resultado * siguiente
        elif operador == "/":
            if siguiente == 0:
                return "Error: division entre 0"
            resultado = resultado / siguiente
        elif operador == "%":
            if siguiente == 0:
                return "Error: modulo entre 0"
            resultado = resultado % siguiente
        else:
            return f"Error: operador '{operador}' no reconocido"
    return resultado

def menu_extra():
    while True:
        print("\n--- Funciones extra de la calculadora ---")
        print("1. Restar dos numeros")
        print("2. Multiplicar dos numeros")
        print("3. Dividir dos numeros")
        print("4. Modulo de dos numeros")
        print("5. Sumar tres numeros")
        print("6. Operaciones mixtas con 3 o mas numeros (ej: 2 + 4 - 3)")
        print("7. Salir")

        opcion = input("Elige una opcion (1-7): ")

        if opcion == "1":
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
            print(f"Resultado: {restar(a, b)}")
        elif opcion == "2":
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
            print(f"Resultado: {multiplicar(a, b)}")
        elif opcion == "3":
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
            print(f"Resultado: {dividir(a, b)}")
        elif opcion == "4":
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
            print(f"Resultado: {modulo(a, b)}")
        elif opcion == "5":
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
            c = float(input("Tercer numero: "))
            print(f"Resultado: {sumar_tres(a, b, c)}")
        elif opcion == "6":
            numeros = list(map(float, input("Numeros separados por espacio: ").split()))
            operadores = input("Operadores separados por espacio: ").split()
            print(f"Resultado: {operaciones_mixtas(numeros, operadores)}")
        elif opcion == "7":
            print("Hasta luego.")
            break
        else:
            print("Opcion no valida, intenta de nuevo.")


menu_extra()


