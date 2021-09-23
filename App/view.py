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
import model

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

def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)

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

def firstThreePieces(result, listsize):
    #'''
    printPieceData(result['elements'][1], result,listsize, 'uno')
    printPieceData(result['elements'][2], result,listsize,'dos')
    printPieceData(result['elements'][3], result,listsize,'tres')
    #'''
    
def lastThreePieces(result, listsize):
    printPieceData(result['elements'][listsize-3],result,listsize, 'menostres')
    printPieceData(result['elements'][listsize-2], result,listsize,'menosdos')
    printPieceData(result['elements'][listsize-1], result,listsize,'menosuno')

#''''
def PiecesID(result, listsize, parametro):
    if parametro == 'uno':
        uno = result['elements'][1]
        IDS = controller.reemplazar(uno)
    elif parametro == 'dos':
        dos = result['elements'][2]
        IDS = controller.reemplazar(dos)
    elif parametro == 'tres':
        tres = result['elements'][3]
        IDS = controller.reemplazar(tres)
    elif parametro == "menostres":
        menostres = result['elements'][listsize-3]
        IDS = controller.reemplazar(menostres)
    elif parametro == "menosdos":
        menosdos = result['elements'][listsize-2]
        IDS = controller.reemplazar(menosdos)
    elif parametro == "menosuno":    
        menosuno = result['elements'][listsize-1]
        IDS = controller.reemplazar(menosuno)

    print(controller.compareid(controller.varioslista(IDS, parametro), parametro))
#'''
def lastThreePiecesOnCatalog(catalog, size):
    printPieceDat(catalog['pieces']['elements'][size - 3])
    printPieceDat(catalog['pieces']['elements'][size - 2])
    printPieceDat(catalog['pieces']['elements'][size - 1])

def printPieceData(piece, result, listsize, param):
    print('Título de la obra: ' + piece['Title'])
    print('Artista: ') 
    PiecesID(result, listsize, param)
    print('Fecha: ' + piece['Date'])
    print('Medio: ' + piece['Medium'])
    print('Dimensiones: ') 
    print(piece['Dimensions']+ '\n'+ '\n') 
  

def printPieceDat(piece):
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

def countPurchase():
    print(controller.countPurchase())


def primeras3pais(lista):
    return controller.primeras3pais(lista)
def encontrarnombres(catalogo):
    controller.encontrarnombres(catalogo)

def buscarids(catalog, titulo):
    return controller.buscarids(catalog, titulo)
    
def imprimirinfo(obtener, catalog):
    
    for word in obtener[0]:
  
        
        titulo = word[0]['Title']
        print(obtener[2][0])
        print('Titulo: ' + str(word[0]['Title']))
        print('Artistas: ' )
        print(buscarids(catalog, titulo))
        print('Fecha de obra: ' + str(word[0]['Date']))
        print('Medio: ' + str(word[0]['Medium']))
        print('Dimensiones: ' + str(word[0]['Dimensions']) + '\n')
        
    for word in obtener[1]:
        titulo = word[0]['Title']
        print(obtener[2][1])
        print('Titulo: ' + str(word[0]['Title']))
        print('Artistas: ' )
        print(buscarids(catalog, titulo))
        print('Fecha de obra: ' + str(word[0]['Date']))
        print('Medio: ' + str(word[0]['Medium']))
        print('Dimensiones: ' + str(word[0]['Dimensions']) + '\n')

        
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos...")
        catalog = initCatalog()
        
        loadData(catalog)
        print(catalog['names'])
        piecesAmmount = lt.size(catalog['pieces'])
        artistsAmmount = lt.size(catalog['artists'])
        print('Obras cargadas: ' + str(piecesAmmount))
        print('Últimas tres obras: \n')
        print(lastThreePiecesOnCatalog(catalog, piecesAmmount))
        print('Artistas cargados: ' + str(artistsAmmount))
        print('Últimos tres artistas: \n')
        print(lastThreeArtistsOnCatalog(catalog, artistsAmmount))
        print('Departamentos existentes cargados: ' + str(lt.size(catalog['departments'])) + '\n')

    elif int(inputs[0]) == 2:
        stYear = input("¿Desde qué año desea empezar a hacer la búsqueda? ")
        fnYear = input("¿Hasta qúe año? ")
        answer = controller.listChronologically(catalog, stYear, fnYear)
        listSize = lt.size(answer[0])
        print('Cantidad total de artistas en el rango: ' + str(listSize) + '\n')
        print('Primeros 3 artistas en el rango: ' + '\n')
        print(firstThreeArtists(answer[0], listSize))
        print('Últimos 3 artistas en el rango: ' + '\n')
        print(lastThreeArtists(answer[0], listSize))
        print('El tiempo que se demoró en ejecutar fue de ' + str(answer[1]) + 'ms.')


    elif int(inputs[0]) == 3:
        beginingyrprev = str(input("¿Desde qué fecha desea empezar a hacer la búsqueda? "))
        beginingyr = float(beginingyrprev[:7].replace("/",".") + beginingyrprev[8:10])
        endingyrprev = str(input("¿Hasta qúe año?  "))
        endingyr = float(endingyrprev[:7].replace("/",".") + beginingyrprev[8:10])
        #print(catalog)
        #'''
        unsortedresult = controller.listChronologicallypieces(catalog, beginingyr, endingyr)

        listSize = lt.size(unsortedresult)
        print(str(unsortedresult['elements'][1]['Title']) + str(unsortedresult['elements'][1]['DateAcquired']))
        
        print('Cantidad total de piezas en el rango: ' + str(listSize) + '\n')
        print('Cantidad de obras adquiridas mediante compra: ')
        comprados = countPurchase()
        print('Primeras 3 obras adquiridas en el rango: ' + '\n')
        print(firstThreePieces(unsortedresult, listSize))
        
        
        print('Últimas 3 piezas adquiridas en el rango: ' + '\n')
        print(lastThreePieces(unsortedresult, listSize))
        #'''
    

    elif int(inputs[0]) == 4:
        authorName = input('¿Qué artista desea clasificar? ')
        answer = controller.classifyByTechnique(catalog, authorName)
        print('Se tienen un total de ' + str(answer[0]) + ' obras del autor en el museo')
        print('El artista hizo uso de ' + str(answer[1]) + ' técnica(s) en estas obras')
        print('Su técnica más usada fue: ' + answer[2])
        print('Esta es la lista de obras en las que usó dicha técnica: \n')
        print(printDatabyTechnique(answer[3]))
        print('El tiempo que se demoró en ejecutar fue de ' + str(answer[4]) + 'ms.')

        
    elif int(inputs[0])==5:
        listaprev = controller.base(catalog)
        
        
        print('Top 10 paises por numero de obras: ' + '\n' + str(listaprev[0])+'\n'+'\n')
        obtener = primeras3pais(listaprev[1])
        imprimirinfo(obtener, catalog)
        #print(catalog['names'])
       
    else:
        sys.exit(0)
sys.exit(0)

