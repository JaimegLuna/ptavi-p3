#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json 
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
 
def pass_list(lista):
    linea = ""
    for elemento in lista:
        linea = linea + elemento[0]
        atr= elemento[1]
        for name in atr:
            linea = linea + '\t' + name + ' = ' + '"' + atr.get(name) + '"'
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
    open_file()
    lista= cHandler.get_tags()
    pass_list(lista)
    archivo_json = open('karaoke.json', 'w') 
    json.dump(lista,archivo_json, sort_keys =True, indent=4, separators=(' ',': '))
    archivo_json.close()

 

    


