#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
 
            
    def new_lista(fichero):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(fichero)
        lista=cHandler.get_tags()
        return lista

    def print_lista(lista)
        
    
    def open_file():
        try:
            fichero=open (sys.argv[1],'r')
            return fichero
        except IndexError:  
            sys.exit("Usage: python3 karaoke.py file.smil")
    
  



if __name__=="main__":

    


