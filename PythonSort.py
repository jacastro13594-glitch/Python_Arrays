'''
Metodo de ordenamiento manual en python usando arreglos
En caso de que la funcion sort() no se pueda usar, podemos utilizar el metodo de ordenamiento burbuja para ordenar el arreglo
'''

#Importacion de librerias
import os

#Funcion para Limpiar la pantalla
def limpiarPantalla():
    os.system('Clear')
    return()

#Declaracion de variables y arreglos
vector = [] #Vector original
valorMaximo = 0 #Almacena cada valor maximo de los indices del vector
numero = 0 #Numero que ingresara el usuario en cada iteracion
cantidad = 0 #Cantidad de numeros que el usuario quiere ordenar
contador = 0 #Contador para incrementar las iteraciones del segundo ciclo while
seguir = str #Variable que verifica si el usuario desea continuar usando el sistema despues de mostrar resultados

#Metodo para pedir la informacion al usuario
while True: #Este ciclo permite repetir el programa hasta que usuario quiera
    vector.clear() #Limpiamos el vector para empezar desde el indice 0
    contador = 1 #Inicializamos el contador para que empiece de 1 nuevamente
    print()
    print('**** Metodo de Ordenacion de una Lista ****')
    print()
    cantidad = int(input('¿Cuantos numeros desea agregar? ')) #Definimos la cantidad de numeros a ordenar por el usuario
    print()
    while contador <= cantidad:
        numero = int(input('Digite un numero entero: '))
        vector.append(numero)
        contador += 1
        n = len(vector)
        vectorCopia = vector.copy()
    
    limpiarPantalla()
    
    for i in range(n-1):
        for j in range(n-1-i):
            if vector[j] > vector[j+1]:
                valorMaximo = vector[j]
                vector[j] = vector[j+1]
                vector[j+1] = valorMaximo
    
    print()
    print('**** Resultados Finales ****')
    print()
    print('Orden Inicial de Datos Ingresados: ')
    print(vectorCopia)
    print()
    print('Datos Ingresados Ordenados de Mayor a Menor: ')
    print(vector)
    print()

    seguir = input('¿Desea seguir ordenar otra lista de numeros? Si/No: ')
    limpiarPantalla()
    if seguir == 'no' or seguir == 'No' or seguir == 'NO':
        input('Digite enter para cerrar el programa...')
        limpiarPantalla()
        break