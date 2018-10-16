# Rubén Villalpando Bremont
# Programa que utiliza ciclos while para cumplir con ciertas tareas.


# Función que recibe el dividendo y el divisor y regresa el cociente y el residuo.
def dividir(dividendo, divisor):
    cociente = 0
    restante = dividendo
    while restante / divisor >= 1:
        restante -= divisor
        cociente += 1
    print(dividendo, " / ", divisor, " = ", cociente, ", sobra ", restante)



# Función que prueba diferentes valores para la función dividir.
def probarDivisiones():
    dividir(15, 6)
    dividir(4, 6)
    dividir(500, 21)
    dividir(151, 32)
    dividir(1024, 8)


# Función que encuentra el mayor en una serie de números dados por el usuario.
def encontrarMayor():
    numeroPedido = 0
    numeroMayor = -2
    print("Teclea una serie de números para encontrar el mayor.")
    while numeroPedido >= 0:    # Va comparando el nuevo número ingresado con el que es mayor.
        numeroPedido = int(input("Teclea un número [-1 para salir]: "))
        if numeroPedido > numeroMayor:
            numeroMayor = numeroPedido
    if numeroMayor >= 0:
        print("El mayor es: ", numeroMayor)
    else:
        print("No hay valor mayor")


# Función principal
def main():
    salio = False
    while salio == False:
        print('''
Misión 07. Ciclos While
Autor: Rubén Villalpando Bremont
Matrícula: A01376331
1. Calcular divisiones
2. Encontrar el mayor
3. Salir 
    ''')
        opcionElegida = int(input("Teclea tu opción: "))
        if opcionElegida == 1:
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            dividir(dividendo, divisor)
        elif opcionElegida == 2:
            encontrarMayor()
        elif opcionElegida == 3:
            salio = True
        else:
            print("ERROR, teclea 1, 2 o 3")


main()