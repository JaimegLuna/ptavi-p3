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
		self.Tunk = Chandler.get_tags()

	def do_local(self):
	"""
	archivos dentro de las URL's
	"""
		doc = ""
		for dic_trunk in self.Trunk:
			for key in dic_trunk:
				doc = doc + key + "/t "
				for key_2 in dic_trunk[key]:
					if str(dic_trunk[key][key_2][0:7] == "http://":
						url = dic_trunk [key][key_2]
						dic_trunk[key][key_2] = url[url.rfind("/")+1:]
						urlretrieve(url)
	
	def __str__(self):
		doc = ""
		for dic_trunk in self.Trunk:
			for key in dic_trunk:
				doc = doc + key + "/t"
				for key_2 in dic_trunk[key]:
					doc = doc + key_2 + '="'+dic_trunk[key][key_2]+ '"' + "/t"
					doc = doc +"/n"
		print(doc)
		return(doc)
	
	def to_json(self, fichero):
		archivo_json = open('Karaoke.json', 'w')
		json.dump(lista, archivo_json, sort_keys =True, indent=4, separators = (' ',': '))
		archivo_json.close()

	

if __name__"__main__":

