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
    

def loadPieces(catalog):
    piecesfile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(piecesfile, encoding='utf-8'))
    for piece in input_file:
        #print(model.fixdatePieces(piece))
        piece = model.fixdatePieces(piece)
        model.addPiece(catalog, piece)   
        

def countPurchase():
    piecesfile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(piecesfile, encoding='utf-8'))
    i=0
    for piece in input_file:
        i = model.countP(piece, i)
    
    return int(i)

#'''''
def compareid(numerodepaquete,param):
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
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


def loadinfo(IDS, piece, file_ca, mayor):
    if type(IDS)==list:
        for artist in file_ca:
            for ID in IDS:
                if ID == artist['ConstituentID']:
                    infotemp= [piece, artist["DisplayName"]]
                    operacionesloadinfo(mayor, artist, infotemp)                        
    else:
        for artist in file_ca:
            if IDS == artist['ConstituentID']:  
                infotemp= [piece, artist["DisplayName"]]
                operacionesloadinfo(mayor, artist, infotemp)  

def operacionesloadinfo(mayor, artist, infotemp):
    for sublist in model.iterator(mayor):
        if model.firstelement(sublist) == artist["Nationality"]:
            model.ponerultimo(sublist, infotemp)
    
def varioslista (IDS, param):
    ID = IDS
    adicional = {}
    if ", " in IDS:
        ID = IDS.split(", ")
        adicionalprev = {param: len(ID)}
        adicional.update(adicionalprev)
    
    return ID, adicional


def reemplazar(uno):
    uno = str(uno["ConstituentID"]).replace("[",'')
    uno =uno.replace(']', '')
    return uno
    #'''    
def fileoc():
    piecesfile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(piecesfile, encoding='utf-8'))
    return input_file
def fileca():
    piecesfile = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(piecesfile, encoding='utf-8'))
    return input_file
def base():
    file_oc = fileoc()
    file_ca = fileca()
    mayor = model.crearlista()
    cargar(mayor, file_oc, file_ca)
    return mayor
def cargar(mayor, file_oc, file_ca):
    nacionalidades = encontrarnacionalidades(file_ca) #encuentra nacionalidades
    for nacionalidad in nacionalidades:
        model.cargarfuncion(mayor, file_oc, file_ca, nacionalidades, nacionalidad)
        
        for piece in file_oc:
            IDSU = reemplazar(piece) #reemplaza los []
            IDS = model.modvarios(IDSU) #divide en lista los ID
            loadinfo(IDS, piece, file_ca, mayor) #agrega piece info en sublista de la nacionalidad
            #print(mayor)
    
def encontrarnacionalidades(file_ca):
    nacionalidades  =[]
    for artist in file_ca:
        if artist["Nationality"] not in nacionalidades:
            nacionalidad =  artist["Nationality"]
            nacionalidades.append(nacionalidad)
    return nacionalidades
        

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

def listChronologically(catalog, stYear, fnYear):
    return model.listChronologically(catalog, stYear, fnYear)

def classifyByTechnique(catalog, authorName):
    return model.classifyByTechnique(catalog, authorName)