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
 """

#from typing_extensions import ParamSpecArgs
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    loadPieces(catalog)
    loadArtists(catalog)
    sortArtists(catalog)
    sortPieces(catalog)
    loadnames(catalog)
    
def loadnames(catalog):
    model.encontrarnombres(catalog)
def loadPieces(catalog):
    piecesfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(piecesfile, encoding='utf-8'))
    for piece in input_file:
        #print(piece['ConstituentID'])
        piece = model.fixdatePieces(piece)
        model.addPiece(catalog, piece)   
        

def countPurchase():
    piecesfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(piecesfile, encoding='utf-8'))
    i=0
    for piece in input_file:
        i = model.countP(piece, i)
    
    return int(i)

#'''''
def compareid(numerodepaquete,param):
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    nombres = ''
    
    for artist in input_file:
        
        if len(numerodepaquete[1]) != 0:
            x = numerodepaquete[1][param]
            
            for o in range(x):
                #print(numerodepaquete[0][o], artist["ConstituentID"])
                if numerodepaquete[0][o] == artist["ConstituentID"]:
                    nombres += 'Artist'+str(o+1)+' ' + artist["DisplayName"]+ '. '
        else:
            if numerodepaquete[0] == artist["ConstituentID"] and len(numerodepaquete[1])==0:
                nombres = artist["DisplayName"]
            
        #'''
    return nombres


def varioslista (IDS, param):
    ID = IDS
    adicional = {}
    if ", " in IDS:
        ID = IDS.split(", ")
        adicionalprev = {param: len(ID)}
        adicional.update(adicionalprev)
    
    return ID, adicional



    #'''    

def base(catalog):
    resultado = model.base(catalog)
    return resultado

def cargar(mayor, catalog):
    
    nacionalidades = model.encontrarnacionalidades(catalog) #encuentra nacionalidades
    resultado = model.cargar(nacionalidades, mayor, catalog)
    return resultado    
    

        

def loadArtists(catalog):
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
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

def listChronologically(catalog, stYear, fnYear):
    return model.listChronologically(catalog, stYear, fnYear)

def classifyByTechnique(catalog, authorName):
    return model.classifyByTechnique(catalog, authorName)

def primeras3pais(lista):
    return model.primeras3pais(lista)

def encontrarnombres(catalogo):
    model.encontrarnombres(catalogo)

def buscarids(catalog, titulo, date):
    return model.buscarids(catalog, titulo, date)

def reemplazar(uno):
    return model.reemplazar(uno)

