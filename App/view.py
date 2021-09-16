"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información al catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")

listType = None

def initCatalog(listType):
    return controller.initCatalog(listType)

def loadData(catalog, listType):
    controller.loadData(catalog, listType)

def firstThreeArtists(artists, size):
    printAuthorData(artists['elements'][1])
    printAuthorData(artists['elements'][2])
    printAuthorData(artists['elements'][3])

def lastThreeArtists(artists, size):
    printAuthorData(artists['elements'][size - 3])
    printAuthorData(artists['elements'][size - 2])
    printAuthorData(artists['elements'][size - 3])

def lastThreeArtistsOnCatalog(catalog, size):
    printAuthorData(catalog['artists']['elements'][size - 3])
    printAuthorData(catalog['artists']['elements'][size - 2])
    printAuthorData(catalog['artists']['elements'][size - 1])

def printAuthorData(author):
    print('Nombre del autor: ' + author['DisplayName'])
    print('Año de nacimiento: ' + author['BeginDate'])
    print('Nacionalidad: ' + author['Nationality'])
    print('Género: ' + author['Gender'] + '\n')

def lastThreePiecesOnCatalog(catalog, size):
    printPieceData(catalog['pieces']['elements'][size - 3])
    printPieceData(catalog['pieces']['elements'][size - 2])
    printPieceData(catalog['pieces']['elements'][size - 1])

def printPieceData(piece):
    print('Título de la obra: ' + piece['Title'])
    print('Tipo de obra: ' + piece['Classification'])
    print('Departamento: ' + piece['Department'] + '\n')

def printDatabyTechnique(piecesList):
    for piece in lt.iterator(piecesList):
        print('Título de la obra: ' + piece['Title'])
        print('Fecha de la obra: ' + piece['Date'])
        print('Medio: ' + piece['Medium'])
        print('Dimensiones: ' + piece['Dimensions'] + '\n')

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        listType = input("¿Desea usar una lista basada en arreglo (1) o una lista simplemente encadenada (2)? ")
        if listType == 1:
            listType = 'ARRAY_LIST'
        elif listType == 2:
            listType == 'SINGLE_LINKED'
        print("Cargando información de los archivos ....")
        catalog = initCatalog(listType)
        loadData(catalog, listType)
        piecesAmmount = lt.size(catalog['pieces'])
        artistsAmmount = lt.size(catalog['artists'])
        print('Obras cargadas: ' + str(piecesAmmount))
        print('Últimas tres obras: \n')
        print(lastThreePiecesOnCatalog(catalog, piecesAmmount))
        print('Artistas cargados: ' + str(artistsAmmount))
        print('Últimos tres artistas: \n')
        print(lastThreeArtistsOnCatalog(catalog, artistsAmmount))
        print('Departamentos existentes cargados: ' + str(lt.size(catalog['departments'])))

    elif int(inputs[0]) == 2:
        stYear = input("¿Desde qué año desea empezar a hacer la búsqueda? ")
        fnYear = input("¿Hasta qúe año? ")
        answer = controller.listChronologically(catalog, stYear, fnYear, listType)
        
        listSize = lt.size(answer)
        print('Cantidad total de artistas en el rango: ' + str(listSize) + '\n')
        print('Primeros 3 artistas en el rango: ' + '\n')
        print(firstThreeArtists(answer, listSize))
        print('Últimos 3 artistas en el rango: ' + '\n')
        print(lastThreeArtists(answer, listSize))

    elif int(inputs[0]) == 4:
        authorName = input('¿Qué artista desea clasificar? ')
        answer = controller.classifyByTechnique(catalog, authorName, listType)
        print('Se tienen un total de ' + str(answer[0]) + ' obras del autor en el museo')
        print('El artista hizo uso de ' + str(answer[1]) + ' técnica(s) en estas obras')
        print('Su técnica más usada fue: ' + answer[2])
        print('Esta es la lista de obras en las que usó dicha técnica: \n')
        print(printDatabyTechnique(answer[3]))

    else:
        sys.exit(0)
sys.exit(0)
