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
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf
from decimal import Decimal
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

def fixdatePieces(piecelist):
    
    stringprev = str(piecelist['DateAcquired'])
    if (len(stringprev)==0):
        piecelist['DateAcquired']=-1
        return piecelist
    i = "0123456789"
    o=0
    for n in stringprev[0:4]:
        if n not in i:
            piecelist['DateAcquired']=-1
            return piecelist       
    year = int(stringprev[0:4]) 

    if len(stringprev) >= 6:
        if stringprev[5] in i:
            month = int(stringprev[5])*0.1
            year = year + month 
            
            if len(stringprev) >= 7:
                if stringprev[6] in i:
                    monthd = int(stringprev[6])*0.01
                    year = year + monthd
                    
                    #'''
                    if len(stringprev) >= 9:
                        if stringprev[8] in i:
                            day = int(stringprev[8])*0.001
                            year = year + day
                            
                            if len(stringprev) == 10:
                                if stringprev[9] in i:
                                    dayd = int(stringprev[9])
                                    dayd = dayd*0.0001
                                    year = year + dayd
                                    year = round(year,4)
                                    #return round(year,4)
    #'''
    piecelist['DateAcquired']=float(year)
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

def modvarios(IDSU):
    ID = IDSU
    if ", " in IDSU:
        ID = IDSU.split(", ")
    return ID

# Funciones de consulta
def listChronologically(catalog, stYear, fnYear):
    artistList = lt.newList('ARRAY_LIST')
    for artist in lt.iterator(catalog['artists']):
        if (artist['BeginDate'] >= stYear) and (artist['BeginDate'] <= fnYear):
            lt.addLast(artistList, artist)
    return artistList

def listChronologicallypieces(catalog, beginingyr, endingyr):
    piecesList = lt.newList('ARRAY_LIST')
    for piece in lt.iterator(catalog['pieces']):
        if (piece['DateAcquired'] >= beginingyr) and (piece['DateAcquired'] <= endingyr):
            lt.addLast(piecesList, piece)
    return piecesList

def crearlista():
    mayor = lt.newList('ARRAY_LIST')
    return mayor

def add(listaprev, file):
    lt.addLast(listaprev, file)

def crearsublistanacionalidades(input_file):
    nacionalidades = lt.newList('ARRAY_LIST')
    for artist in input_file:
        if lt.isPresent(nacionalidades,artist["Nationality"])==0 :
            lt.addLast(nacionalidades, artist["Nationality"])
    return nacionalidades


def classifyByTechnique(catalog, authorName):
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

    return totalPieces, totalTechniques, mostUsedTechnique['name'], mostUsedTechnique['piecesList']


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
    merge.sort(catalog['pieces'], comparedate)
    