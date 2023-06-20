def suma(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

def resta(valor1, valor2):
    resultado = valor1 - valor2
    return resultado

def multiplicacion(valor1, valor2):
    resultado = valor1 * valor2
    return resultado

def division(valor1, valor2):
    if valor2 != 0:
        resultado = valor1 / valor2
    else:
        print("No es posible dividir por cero.")
        resultado = None
    return resultado

def porcentaje(valor1, valor2):
    resultado = (valor1 / 100) * valor2
    return resultado

def raiz_cuadrada(valor1):
    resultado = valor1 ** (1 / 2)
    return resultado

def raiz_cubica(valor1):
    resultado = valor1 ** (1 / 3)
    return resultado

# Bloque principal
resultado = []
print("Bienvenido a la calculadora en Python.")
while True:
    print("Elegir qué operación realizar:")
    print("1) Sumar")
    print("2) Restar")
    print("3) Dividir")
    print("4) Multiplicar")
    print("5) Porcentajes")
    print("6) Raíz Cuadrada")
    print("7) Raíz Cúbica")
    print("8) Salir")

    n = input("Seleccionar operación con números:")

    if n == "8":
        print("Muchas gracias por utilizar la calculadora")
        break

    print("En caso de seleccionar raíces, omitir segundo valor")
    valor1 = int(input("Ingresar primer valor: "))

    if n not in ["6", "7"]:
        valor2 = int(input("Ingresar segundo valor: "))
    else:
        valor2 = None

    if n == "1":
        resultado = suma(valor1, valor2)
    elif n == "2":
        resultado = resta(valor1, valor2)
    elif n == "3":
        resultado = division(valor1, valor2)
    elif n == "4":
        resultado = multiplicacion(valor1, valor2)
    elif n == "5":
        resultado = porcentaje(valor1, valor2)
    elif n == "6":
        resultado = raiz_cuadrada(valor1)
    elif n == "7":
        resultado = raiz_cubica(valor1)
    else:
        print("Por favor seleccione una opción válida.")

    print("El resultado es:", resultado)
    resultado = []
