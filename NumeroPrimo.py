'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''

#Funcion que define si el numero es primo
def numeroPrimo(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
            else:
                return True

#Variables Globales
n = 1

print()
print('**** LISTA DE NUMEROS PRIMOS DEL 1 A 100 ****')
print()
#Ciclo para recorrer los 100 numeros del enunciado
while n <= 100:
    if(numeroPrimo(n) == True): #Llamado y validacion de la funcion numeroPrimo, si es verdadero, imprimira el numero primo
        print(n)
    n += 1
print()
input('Presione la tecla Enter para continuar...')