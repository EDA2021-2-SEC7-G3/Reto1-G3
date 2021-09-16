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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(listType):
    catalog = model.newCatalog(listType)
    return catalog

# Funciones para la carga de datos
def loadData(catalog, listType):
    loadPieces(catalog, listType)
    loadArtists(catalog)
    sortArtists(catalog)
    sortPieces(catalog)
    
def loadPieces(catalog, listType):
    piecesfile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(piecesfile, encoding='utf-8'))
    for piece in input_file:
        piece = model.fixdatePieces(piece)
        model.addPiece(catalog, piece, listType)   
        
def countPurchase():
    piecesfile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(piecesfile, encoding='utf-8'))
    i=0
    for piece in input_file:
        i = model.countP(piece, i)
    return int(i)

def compareid(uno, dos, tres, menostres, menosdos, menosuno):
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    dicnombres = {}
    
    for artist in input_file:
       
        if (uno == artist["ConstituentID"]):
            
            dictemp = {'uno':artist["DisplayName"]}
            dicnombres.update(dictemp)
        
    
        if (dos == artist["ConstituentID"]):
            
            dictemp = {'dos':artist["DisplayName"]}
            dicnombres.update(dictemp)
   
        if (tres == artist["ConstituentID"]):
            
            dictemp = {'tres':artist["DisplayName"]}
            dicnombres.update(dictemp)
        if (menostres == artist["ConstituentID"]):
           
            dictemp = {'menostres':artist["DisplayName"]}
            dicnombres.update(dictemp)
        if (menosdos == artist["ConstituentID"]):
           
            dictemp = {'menosdos':artist["DisplayName"]}
            dicnombres.update(dictemp)
        if (menosuno == artist["ConstituentID"]):
            
            dictemp = {'menosuno':artist["DisplayName"]}
            dicnombres.update(dictemp)
            #'''
    return dicnombres

def reemplazar(uno):
    uno = str(uno["ConstituentID"]).replace("[",'')
    uno =uno.replace(']', '')
    return uno
    #'''    


def loadArtists(catalog):
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

# Funciones de ordenamiento

def sortArtists(catalog):
    model.sortArtists(catalog)

def sortPieces(catalog):
    model.sortPieces(catalog)


# Funciones de consulta sobre el catálogo
def listChronologicallypieces(catalog, beginingyr, endingyr):
    return model.listChronologicallypieces(catalog, beginingyr, endingyr)

def listChronologically(catalog, stYear, fnYear, listType):
    return model.listChronologically(catalog, stYear, fnYear, listType)

def classifyByTechnique(catalog, authorName, listType):
    return model.classifyByTechnique(catalog, authorName, listType)