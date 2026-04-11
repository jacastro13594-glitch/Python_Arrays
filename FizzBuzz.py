'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

#Declaracion de variables
contador = 1

#Ciclo para definir si los numeros son divisibles entre 3 y 5
while contador <= 100:
    if contador % 3 == 0 and contador % 5 == 0:
        print(contador, ': fizzbuzz')
        print()
    elif contador % 3 == 0:
        print(contador, ': fizz')
        print()
    elif contador % 5 == 0:
        print(contador, ': buzz')
        print()
    contador += 1