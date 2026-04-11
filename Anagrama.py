'''
* Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''

#Funcion para comparar las dos palabras
def anagrama(palabra1, palabra2):
    #Se convierten ambas palabras en minusculas para evitar diferencias por mayusculas
    p1 = palabra1.lower()
    p2 = palabra2.lower()
    resultado = bool

    #Se compara si ambas palabras son iguales ordenandolas
    if sorted(p1) == sorted(p2):
        resultado
    else:
        resultado = False
    return(resultado)

#Variables Globales
primerPalabra = str
segundaPalabra = str

#Solicitud de ambas palabras al usuario
print()
print('**** ANAGRAMAS ****')
print()
primerPalabra = input('Ingrese la primer palabra: ')
print()
segundaPalabra = input('Ingrese la segunda palabra: ')
print()
#Llamado a la funcion anagrama y comparacion de valor
if anagrama(primerPalabra, segundaPalabra):
    print('Las palabras ingresadas son anagramas')
else:
    print('Las palabras ingresadas no son anagramas')
print()
input('Digite la tecla Enter para continuar...')