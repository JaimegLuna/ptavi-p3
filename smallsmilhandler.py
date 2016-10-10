#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
		"""
        Constructor. Inicializamos las variables
        """

        self.etiquetas = []

        self.lista = {'root-layout':['width', 'height', 'background-color'], 
					'region':['id', 'top', 'bottom', 'left', 'right'],
					'img':['src', 'region', 'begin', 'dur'],
					'audio':['src', 'begin', 'dur'],
					'textstream':['src', 'region']}

		self.atr={}

	def startElement(self, name, attrs):
		"""
        Método que se llama cuando se abre una etiqueta
        """
		if name == 'self.lista': 
		#Asi cogemos todos los atributos de mi diccionario y no tengo que hacer varios if
			for name in self.etiquetas: #iteramos por el diccionario 
				self.atr = attrs.get('valor', "")
            self.nueva_lista(name, slef.atributo)
	
	def get_tags(self):
		return self.etiquetas

	def nueva_lista(self, nombre, atributos):
        etiqueta=[]
        self.etiqueta= self.endetiqueta(name)
		self.etoqueta= self.endetiqueta(atributo)


	def print()
		return self.lista 
        
		
		





		
if __name__=="__main__":
	 """
    Programa principal
    """
    parser = make_parser()
    cHandler = ChistesHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('chistes2.xml'))
