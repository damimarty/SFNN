#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from network import Network

class Population(object):
	def __init__(self, nbPeople, nbNeurons = 5, nbConnexions = 5, nbInputs = 2, nbOutputs = 1):
		self.nbPeople = 0
		self.peopleList = []
		for idPeople in range(nbPeople):
			self.createNetwork(nbNeurons, nbConnexions)

	def createNetwork(self, nbNeurons, nbConnexions):
		self.peopleList.append(Network(nbNeurons, nbConnexions))
		self.nbPeople += 1

	def run(self, nbTimes = 1):
		for time in range(nbTimes):
			for idPeople in range(self.nbPeople):
				self.peopleList[idPeople].evaluateNetwork()
