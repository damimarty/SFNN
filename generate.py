#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from network import Network

def generate(name =  "master.gen"):
	while(True):
		g = Network(7, 14, 2, 1)
		g.draw("master")
		c = raw_input("save this net: ")
		if c == "y":
			g.save(name)
			break

generate()
