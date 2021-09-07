"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'pieces': None,
               'artists': None,
               'departments': None}
    
    catalog['pieces'] = lt.newList('ARRAY_LIST')
    catalog['artists'] = lt.newList('ARRAY_LIST')
    catalog['departments'] = lt.newList('ARRAY_LIST',
                                        cmpfunction=comparedepartments)

    return catalog
               
# Funciones para agregar informacion al catalogo
def addPiece(catalog, piece):
    lt.addLast(catalog['pieces'], piece)

    department = piece['Department']
    addDepartment(catalog, department, piece)

def addDepartment(catalog, departmentName, piece):
    departmentsList = catalog['departments']
    posDepartment = lt.isPresent(departmentsList, departmentName)
    if posDepartment > 0:
        department = lt.getElement(departmentsList, posDepartment)
    else:
        department = newDepartment(departmentName)
        lt.addLast(departmentsList, department)
    lt.addLast(department['pieces'], piece['Title'])

def addArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)

# Funciones para creacion de datos
def newDepartment(name):
    department = {'name': "", 'pieces': None}
    department['name'] = name
    department['pieces'] = lt.newList('ARRAY_LIST')
    return department

# Funciones de consulta

def listChronologically(catalog, stYear, fnYear):
    artistsFromCatalog = catalog['artists']['elements']
    aFCSize = lt.size(catalog['artists'])
    artistList = lt.newList('ARRAY_LIST')

    for cont in range(0, aFCSize):
        artist = (artistsFromCatalog[cont])
        if (artist['BeginDate'] >= stYear) and (artist['BeginDate'] <= fnYear):
            lt.addLast(artistList, artist)

    return artistList

def classifyByTechnique(catalog, authorName):
    authorPos = lt.isPresent(catalog['artists'], authorName)
    author = lt.getElement(catalog['artists'], authorPos)
    authorID = author['ConstituentID']

    piecesFromCatalog = catalog['pieces']['elements']
    pFCSize = int(len(piecesFromCatalog))

    piecesAndTechniques = {'allPieces': lt.newList('ARRAY_LIST'), 'allTechniques': lt.newList('ARRAY_LIST')}
    
    for cont in range (0, pFCSize):
        piece = (piecesFromCatalog[cont])
        if authorID in piece['ConstituentID']:
            lt.addLast(piecesAndTechniques['allPieces'], piece)
            if piece['Medium'] not in piecesAndTechniques['allTechniques']['elements']:
                lt.addLast(piecesAndTechniques['allTechniques'], piece['Medium'])

    piecesSize = lt.size(piecesAndTechniques['allPieces'])
    techniquesSize = lt.size(piecesAndTechniques['allTechniques'])
    ans1 = piecesSize, techniquesSize
    ans2 = {'techniques': lt.newList('ARRAY_LIST')}

    for cont in range(0, piecesSize):
        piece = piecesAndTechniques['allPieces']['elements'][cont]
        posTechnique = lt.isPresent(ans2['techniques'], piece['Medium'])
        if posTechnique > 0:
            technique = lt.getElement(ans2['techniques'], posTechnique)
        else:
            technique = newDepartment(piece['Medium'])
            lt.addLast(ans2['techniques'], technique)
        lt.addLast(ans2['techniques']['elements']['pieces'], piece)

    for cont in range(0, lt.size(ans2['techniques'])):
        
    

# Funciones utilizadas para comparar elementos dentro de una lista
def comparedepartments(department1, department2):
    if (department1.lower() in department2['name'].lower()):
        return 0
    return -1

def comparebirthday(firstArtist, secondArtist):
    return (int(firstArtist['BeginDate']) < int(secondArtist['BeginDate']))

# Funciones de ordenamiento
def sortArtists(catalog):
    sa.sort(catalog['artists'], comparebirthday)
