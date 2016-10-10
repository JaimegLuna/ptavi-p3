#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.etiquetas = []

        self.lista = {'root-layout':['width', 'height', 'background-color'], 
                    'region':['id', 'top', 'bottom', 'left', 'right'],
                    'img':['src', 'region', 'begin', 'dur'],
                    'audio':['src', 'begin', 'dur'],
                    'textstream':['src', 'region']}

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name in self.lista: 
        #Asi cogemos todos los atributos de mi diccionario y no tengo que hacer varios if
        #iteramos por el diccionario 
            self.atr={}
            for valor in self.lista[name]:
                self.atr[valor] = attrs.get(valor, "")
            self.nueva_lista(name, self.atr)

    
    def get_tags(self):
        return self.etiquetas

    def nueva_lista(self, nombre, atr):
        etiqueta=[]
        etiqueta.append(nombre)
        etiqueta.append(atr)
        self.etiquetas.append(etiqueta)
        return self.etiquetas

def print_etiqueta(etiquetas):
    for elementos in etiquetas:
        print(elementos)
    
if __name__=="__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open("karaoke.smil"))
    print_etiqueta(cHandler.get_tags())
