#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSmillHandler(ContenetHandler):
	"""
	Esta clase se utiliza para utilizar un fichero SMIL
	"""

	def __init__(self):
	"""
	Con esto, inicializamos las variables
	"""
		
		self.lista = []
		self.dic = {'root-layout': ['width', 'height','background-color'],	
			'region': ['id', 'top', 'bottom', 'left', 'right'],
			'img': ['src', 'region', 'begin', 'dur'],
			'audio': ['src', 'begin', 'dur'],
			'textstream': ['src', 'region']}

	def get_tags(self):
   
