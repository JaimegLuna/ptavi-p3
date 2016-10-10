#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json 
import urllib
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        self.cHandler = SmallSMILHandler()
        parser.setContentHandler(self.cHandler)
        parser.parse(open(fichero))

    def __str__(self):
        linea = ""
        for elemento in self.lista:
            linea = linea + elemento[0]
            atr= elemento[1]
            for name in atr:
                linea = linea + '\t' + name + ' = ' + '"' + atr.get(name) + '"'
            linea = linea + '\n'
        print (linea)

    def to_json(self, fichero):
        archivo_json = open('karaoke.json', 'w') 
        json.dump(lista,archivo_json, sort_keys =True, indent=4, separators=(' ',': '))
        archivo_json.close()

    def do_local(self):
        for linea in self.lista:
            if isinstance(linea, dict):
                if 'src' in linea:
                    url_list.append(line['src'])
        return(url_list)

    def print_url(url_list):
        for linea in url_list:   
            fich=linea.split('/')[-1]
            try:
                urllib.request.urlretrieve(linea,fich)
            except ValueError:
                sys.exit("It is NOt an URL")
                    
        if linea['src'] == 'http':
            local=linea['src'].split('/')[-1]
            urllib.request.urlretrieve(linea['src'],local)

if __name__=="__main__":
    try:
        archivo=sys.argv[1]
        fichero= sys.argv[1]
    except IndexError:  
        sys.exit("Usage: python3 karaoke.py file.smil")

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(sys.argv[1]))
    
    try:
        karaoke=KaraokeLocal(fichero)
    except FileNotFoundError:
        sys.exit("Error:File not found")

    archivo_json = open('karaoke.json', 'w') 
    json.dump(cHandler.get_tags(),archivo_json, sort_keys =True, indent=4, separators=(' ',': '))
    archivo_json.close()
    print(karaoke)
    karaoke.to_json(fichero)
    karaoke.do_local()
    karaoke.to_json(fichero,'local')
    print(karaoke)
    
    url_lista = busca_url(cHandler.get_tags())
    archivo_url(url_lista)     
