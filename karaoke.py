#!/usr/bin/python3)
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
		CHandler = SmallSMILhandler()
		parser.setContentHandler(CHandler)
		parser.parse(open(fichero))
	
	def __str__(self):
	
	def to_json(self, fichero):
		archivo_json = open('Karaoke.json', 'w')
		json.dump(lista, archivo_json, sort_keys =True, indent=4, separators = (' ',': '))
		archivo_json.close()

	def do_local(self):

if __name__"__main__":

