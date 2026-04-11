'''
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
'''

#Declaracion de variables
numero1 = 0
numero2 = 1
numero3 = 0
contador = 0

print()
print('**** SECUENCIA FIBONNACCI ****')
#Ciclo para crear la secuencia Fibonacci
for i in range(0, 50):
    print(numero3)
    numero3 = numero1 + numero2
    numero1 = numero2
    numero2 = numero3
