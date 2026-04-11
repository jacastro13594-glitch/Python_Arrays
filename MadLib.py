'''
Juego MadLib
'''

#Importacion de Librerias
from random import randint
import copy

#Crear la variable para almacenar la historia
historia = (
    'Este fin de semana voy a acampar con {}. Empaqué mi linterna, saco de dormir, y '
    '{}. Estoy tan {} para {} en una tienda de campaña. Estoy '
    '{} que vamos a ver un(a) {}, que son peligrosos. Vamos a caminar, pescar, y '
    '{}. He oído que el lago {} es genial para {}. Entonces '
    'vamos a caminar {} por del bosque para {} {}. Si veo un(a) '
    '{} {} mientras estoy caminando, ¡lo llevaré a casa como mascota! Por la '
    'noche vamos a contar {} {} historias y asar alrededor de la fogata!!'
)

#Crear un diccionario de datos para extraer las palabras por tipo
palabraDiccionario = {
    'nombre': ['Cinthia', 'Jorge', 'Macarena', 'Capuchino', 'Chente'],
    'sustantivo': ['Mesa', 'Perro', 'Gato', 'Carro', 'Casa'],
    'adjetivo': ['Lindo', 'Alto', 'Bajo', 'Suave', 'dormilon'],
    'verbo': ['Comer', 'Dormir', 'Jugar', 'Brincar', 'Correr'],
    'adjetivo': ['Tierna', 'Amorosa', 'Largo', 'Inquieta', 'Energica'],
    'animal': ['Perro', 'Gato', 'Chancho', 'Marrano', 'Cerdo'],
    'verbo': ['Caminar', 'Maullar', 'Ladrar', 'Excavar', 'Saltar'],
    'color': ['Cafe', 'Carey', 'Gris', 'Capuchino', 'Blanco'],
    'verbo': ['Hablar', 'Sentar', 'Acostar', 'Parar', 'Caminar'],
    'adverbio': ['Hablantin', 'Comelon', 'Fit', 'Enano', 'Pancilla'],
    'numero': [1, 4, 3, 2, 5],
    'medidaTiempo': ['1 Hora', '30 minutos', '5 minutos', '4 horas', '15 minutos'],
    'animal': ['Cabra', 'Ganzo', 'Vaca', 'Ternero', 'Pato'],
    'color': ['Negro', 'Azul', 'Verde', 'Celeste', 'Rosado'],
    'numero': [5,  9, 10, 7, 56, 7],
    'palabraTonta': ['Bobo', 'Tontin', 'Waka', 'Papitostis', 'Caquero'],
    'sustantivoPlural': ['Casas', 'Perros', 'Gatos', 'Carros', 'Patos'],
}

#Funcion para obtener cada palabra para asiganarla a cada espacio vacio, evitando que una palabra ya usada se repita
def obtenerPalabra(type, diccionarioLocal):
    palabras = diccionarioLocal[type]
    contador = len(palabras)-1
    index = randint(0, contador)
    return diccionarioLocal[type].pop(index) 

#Funcion para crear la historia con las palabras aleatoriamente
def crearHistoria():
    palabraLocal = copy.deepcopy(palabraDiccionario)
    return historia.format(
        obtenerPalabra('nombre', palabraLocal),
        obtenerPalabra('sustantivo', palabraLocal),
        obtenerPalabra('adjetivo', palabraLocal),
        obtenerPalabra('verbo', palabraLocal),
        obtenerPalabra('adjetivo', palabraLocal),
        obtenerPalabra('animal', palabraLocal),
        obtenerPalabra('verbo', palabraLocal),
        obtenerPalabra('color', palabraLocal),
        obtenerPalabra('verbo', palabraLocal),
        obtenerPalabra('adverbio', palabraLocal),
        obtenerPalabra('numero', palabraLocal),
        obtenerPalabra('medidaTiempo', palabraLocal),
        obtenerPalabra('animal', palabraLocal),
        obtenerPalabra('color', palabraLocal),
        obtenerPalabra('numero', palabraLocal),
        obtenerPalabra('palabraTonta', palabraLocal),
        obtenerPalabra('sustantivoPlural', palabraLocal)
    )

#Llaamamos a la funcion de Crear Historia para imprimir una historia con los datos del diccionario
print()
print('**** JUEGO MAD LIB ****')
print()
print('**** VAMOS A ACAMPAR 1 ****')
print()
print(crearHistoria())
print()