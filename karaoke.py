#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
 
            
def new_list(archivo):
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(archivo)
    list=cHandler.get_tags()
    return list       

def pass_list(lista):
    linea = ""
    for elemento in lista:
        linea = linea + elemento[0]
        atr= elemento[1].dato()
        for name, atributo in atr:
            linea = linea + '\t' + name + ' = ' + '"' + atributo + '"'
        linea = linea + '\n'

    print (linea)

def open_file():
    try:
        archivo=open(sys.argv[1],'r')
        return archivo
    except IndexError:  
        sys.exit("Usage: python3 karaoke.py file.smil")

if __name__=="__main__":

    fichero = open_file()
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(fichero)
    print(cHandler.get_tags())
    lista = new_list(fichero)
    pass_lista(lista)

    


