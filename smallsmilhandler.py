#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

# No se como solucionar el problema que me da el pep8 (error w191 "Identation contains tabs)


class SmallSmillHandler(ContenetHandler):
	"""
	Esta clase se utiliza para utilizar un fichero SMIL
	"""

	def __init__(self):
	"""
	Con esto, inicializamos las variables
	"""
		self.lista = []
		self.dic = {'root-layout': ['width', 'height', 'background-color'],	
			'region': ['id', 'top', 'bottom', 'left', 'right'],
			'img': ['src', 'region', 'begin', 'dur'],
			'audio': ['src', 'begin', 'dur'],
			'textstream': ['src', 'region']}

	def start(self, name, atrib):
	"""
	para abrir una etiqueta
	"""
	
		if name in self.dic:
		# asi vamos escogiendo atributo a atributo de la lista 
			print(name)
			for atributo in self.dic[name]:
				self.atrib = {}
				self.atrib[atributo] = atrib.get(atributo, "")
				self.lista.appenjd(self.atri)


	def get_tags(self):
		return self.lista


if __name__=="__main__":
	
	CHandler = SmallSmilHandler()
	parser = make_parser()
	parser.setContentHandler(CHandler)
	parser.parse(open('karaoke.smil'))
	# Karaoke.smil es un ejemplo, una prueba de que funciona con smil
	
	print(CHandler.get_tags())   

