#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from genetics import Genetics
from network import Network
import matplotlib.pyplot as plt
import random

class latchRS(object):
	def __init__(self):
		self.output = 0.2

	def run(self, inputArray):
		iSet, iReset = inputArray
		if iSet == 1.0 and iReset == 0.0:
			self.output = 0.8
		if iSet == 0.0 and iReset == 1.0:
			self.output = 0.2
		if iSet == 1.0 and iReset == 1.0:
			if self.output == 0.8:
				self.output = 0.2
			else:
				self.output = 0.8
		return self.output

def testPool():
	latch = latchRS()
	base = Network(10, 10, 2, 1)
	baseGenome = base.getGenes()
	pool = Genetics(genome = baseGenome)
	nEvaluation = 20
	nRetain = 5
	individualSpecies = []
	speciesData = []
	fitnesses = []
	# nb generation
	for age in range(50):
		for people in pool.generationN.peopleList:
			error = 0.0
			for i in range(nEvaluation):
				iSet = 1.0 if random.random() > 0.9 else 0.0
				iReset = 1.0 if random.random() < 0.1 else 0.0
				for j in range(nRetain):
					inputArray = [iSet, iReset]
					expected = latch.run(inputArray)
					people.evaluateNetwork()
					error += abs(people.getOutput()[0]- expected)
			people.setFitness((nEvaluation*nRetain)/error)
		print("next age: %d"%(age))
		fitnesses.append(pool.generationN.getBestFitness())
		pool.step()
		sp = pool.getSpieces()
		for gsp,c in sp:
			if gsp not in individualSpecies:
				individualSpecies.append(gsp)
		speciesData.append(sp)
		pool.loop()

	evolution = [[] for i in range(len(individualSpecies))]
	print(len(evolution))

	for data in speciesData:
		for g in individualSpecies:
			found = False
			for genome,count in data:
				#print(genome,g)
				if Network.isSameGenome(genome,g):
					found = True
					evolution[individualSpecies.index(genome)].append(count)
			if not found:
				evolution[individualSpecies.index(g)].append(0)

	for speEvo in evolution:
		plt.plot(speEvo)

	plt.figure()
	plt.plot(fitnesses)
	plt.show()

testPool()
