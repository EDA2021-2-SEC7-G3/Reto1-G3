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
import time

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
    catalog['departments'] = lt.newList('ARRAY_LIST', cmpfunction=comparedepartments)
    return catalog
               
# Funciones para agregar informacion al catalogo
def addPiece(catalog, piece):
    lt.addLast(catalog['pieces'], piece)
    department = piece['Department']
    addDepartment(catalog, department, piece)

def fixdatePieces(piecelist):
    stringprev = str(piecelist['DateAcquired'])
    year = stringprev[0:4]
    if type(year) == int:
        year = int(year)
    if len(stringprev) == 6:
        if type(stringprev[5])==int:
            month = int(stringprev[5])*0.1
            year = year + month
    if len(stringprev) == 7:
        if type(stringprev[6])==int:
            monthd = int(stringprev[6])*0.01
            year = year + monthd
    if len(stringprev) == 9:
        if type(stringprev[8])==int:
            day = int(stringprev[8])*0.001
            year = year + day
    if len(stringprev) == 10:
        if type(stringprev[9])==int:
            dayd = int(stringprev[9])*0.0001
            year = year + dayd
    if len(stringprev)==0:
        year = 0
    piecelist['DateAcquired']=int(year)
    return piecelist

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

def newTechnique(name):
    technique = {'name': "", 'pieces': None}
    technique['name'] = name
    technique['pieces'] = lt.newList('ARRAY_LIST')
    return technique

def countP(piece, i):
    if 'Purchase' in piece['CreditLine']:
        i+=1
    return i

# Funciones de consulta
def listChronologically(catalog, stYear, fnYear):
    startTime = time.process_time()
    artistList = lt.newList('ARRAY_LIST')
    for artist in lt.iterator(catalog['artists']):
        if (artist['BeginDate'] >= stYear) and (artist['BeginDate'] <= fnYear):
            lt.addLast(artistList, artist)
    stopTime = time.process_time()
    elapsedTime = (stopTime - startTime) * 1000
    return artistList, elapsedTime

def classifyByTechnique(catalog, authorName):
    startTime = time.process_time()
    authorID = None
    for artist in lt.iterator(catalog['artists']):
        if artist['DisplayName'] == authorName:
            authorID = artist['ConstituentID']
    piecesByTechniques = {'techniques': None}
    piecesByTechniques['techniques'] = lt.newList('ARRAY_LIST', cmpfunction=comparetechniques)
    for piece in lt.iterator(catalog['pieces']):
        if authorID in piece['ConstituentID']:
            techniquePos = lt.isPresent(piecesByTechniques['techniques'], piece['Medium'])
            if techniquePos > 0:
                technique = lt.getElement(piecesByTechniques['techniques'], techniquePos)
            else:
                technique = newTechnique(piece['Medium'])
                lt.addLast(piecesByTechniques['techniques'], technique)
            lt.addLast(technique['pieces'], piece)
    totalPieces = 0
    totalTechniques = lt.size(piecesByTechniques['techniques'])
    mostUsedTechnique = {'name': None, 'piecesList': None, 'mostPieces': 0}
    for technique in lt.iterator(piecesByTechniques['techniques']):
        ammPieces = lt.size(technique['pieces'])
        totalPieces += ammPieces
        if ammPieces > mostUsedTechnique['mostPieces']:
            mostUsedTechnique['name'] = technique['name']
            mostUsedTechnique['piecesList'] = technique['pieces']
            mostUsedTechnique['mostPieces'] = ammPieces
    stopTime = time.process_time()
    elapsedTime = (stopTime - startTime) * 1000
    return totalPieces, totalTechniques, mostUsedTechnique['name'], mostUsedTechnique['piecesList'], elapsedTime

# Funciones utilizadas para comparar elementos dentro de una lista
def comparedepartments(department1, department2):
    if (department1.lower() in department2['name'].lower()):
        return 0
    return -1

def comparetechniques(technique1, technique2):
    if (technique1.lower() in technique2['name'].lower()):
        return 0
    return -1

def comparebirthday(firstArtist, secondArtist):
    return (int(firstArtist['BeginDate']) < int(secondArtist['BeginDate']))

def comparedate(firstyear, secondyear):
    return (int(firstyear['DateAcquired']) < int(secondyear['DateAcquired']))

# Funciones de ordenamiento
def sortArtists(catalog):
    sa.sort(catalog['artists'], comparebirthday)

def sortPieces(catalog):
    sa.sort(catalog['pieces'], comparedate)