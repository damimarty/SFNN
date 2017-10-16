#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from network import Network

class Population(object):
	def __init__(self, nbPeople, nbNeurons = 5, nbConnexions = 5, nbInputs = 2, nbOutputs = 1, genomes = None):
		self.peopleList = []
		if genomes is None:
			for j in range(nbPeople):
				self.createNetwork(nbNeurons, nbConnexions, nbInputs, nbOutputs, None)
		else:
			for i in range(divisions):
				for j in range(nbPeople/divisions):
					self.createNetwork(nbNeurons, nbConnexions, nbInputs, nbOutputs, genomes[i])

	def createNetwork(self, nbNeurons = 5, nbConnexions = 5, nbInputs = 2, nbOutputs = 1, genome = None):
		self.peopleList.append(Network(nbNeurons, nbConnexions, nbInputs, nbOutputs, genome))

	def run(self, nbTimes = 1):
		for time in range(nbTimes):
			for people in self.peopleList:
				self.people.evaluateNetwork()

	def getPopulation(self):
		return self.peopleList

	def setPopulation(self, data):
		self.peopleList = list(data)

	def sortByFitness(self):
		self.peopleList = sorted(self.peopleList, key = lambda people: -people.getFitness())

	def getBestFitness(self):
		return max([p.getFitness() for p in self.peopleList])

	def clean(self):
		self.peopleList = []

	def extend(self,array):
		self.peopleList.extend(array)

	def append(self,item):
		self.peopleList.append(item)

	def getFirsts(self,index):
		return list(self.peopleList[0:index])

	def size(self):
		return len(self.peopleList)

	def __str__(self):
		ret = ""
		for people in self.peopleList:
				ret += "\n "+ str(people.getFitness())
		return ret

	def getSpieces(self):
		spieces = []
		count = []
		for n in self.peopleList:
			g = n.getGenes()
			found = False
			for i in range(len(spieces)):
				spiece, count = spieces[i]
				if Network.isSameGenome(spiece,g):
					spieces[i] = (g,count+1)
					found = True
					break
			if not found:
				spieces.append((g,1))
		return spieces

	def getGenotypes(self):
		spieces = []
		count = []
		for n in self.peopleList:
			nbN, nbC = n.getGenotype()
			found = False
			for i in range(len(spieces)):
				(nbNn, nbCc), count = spieces[i]
				if nbNn == nbN and nbCc == nbC:
					spieces[i] = ((nbN, nbC),count+1)
					found = True
					break
			if not found:
				# print "not found"
				spieces.append(((nbN, nbC),1))
		return spieces
