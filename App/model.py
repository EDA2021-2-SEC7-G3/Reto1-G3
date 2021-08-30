﻿"""
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

# Funciones utilizadas para comparar elementos dentro de una lista
def comparedepartments(department1, department2):
    if (department1.lower() in department2['name'].lower()):
        return 0
    return -1

# Funciones de ordenamiento