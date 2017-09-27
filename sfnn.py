#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

import math
import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer

from connexion import Connexion
from neuron import Neuron
from network import Network
from population import Population
from genetics import Genetics

def testNetwork():
	nbNeurons = 10
	nbConnexions = 15
	george = Network(nbNeurons, nbConnexions)
	george.evaluateNetwork()
	george.printNetwork()
	start = timer()
	for i in range(100):
		george.evaluateNetwork()
	george.evaluateNetwork()
	end = timer()
	george.printNetwork()
	print(end - start)
	george.draw()

def testNetwork2():
	nbNeurons = 10
	nbConnexions = 15
	george = Network(nbNeurons, nbConnexions)
	ggenes = george.getGenes()
	print(ggenes)
	# george.draw()
	francis = Network(genes=ggenes)
	fgenes = francis.getGenes()
	print(fgenes)

def testGenetics():
	base = Network(5, 2, 2, 1)
	baseGenome = base.getGenes()
	pool = Genetics(nbPeople = 30, genome = baseGenome)

	individualSpecies = []
	speciesData = []

	for i in range(50):
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

	plt.show()

	#for d in speicesData

def testOutputNetwork():
	nbNeurons = 10
	nbConnexions = 250
	nbRuns = 3140
	nbInputs = 2
	nbOutputs = 1
	george = Network(nbNeurons, nbConnexions,nbInputs,nbOutputs)
	outputs = [[v] for v in george.extractNeuronsOutputs()]
	netOutput = [[v] for v in range(nbOutputs)]
	for i in range(nbRuns):
		inputArray = [math.sin(float(i)/100.0)/2.0 + 0.5,math.cos(float(i)/100.0)/2.0 + 0.5]
		george.setInput(inputArray)
		george.evaluateNetwork()
		for (prevOutputList,output) in zip(outputs,george.extractNeuronsOutputs()):
			prevOutputList.append(output)
		for (prevNetOutput,output) in zip(netOutput,george.getOutput()):
			prevNetOutput.append(output)

	plt.figure()
	for outputList in outputs:
	    plt.plot(outputList)

	plt.figure()
	for netOutputList in netOutput:
		plt.plot(netOutputList)

	plt.show()

def testPopulation():
	nbPeople = 10
	nbNeurons = 50
	nbConnexions = 80
	start = timer()
	ofTheJungle = Population(nbPeople, nbNeurons, nbConnexions)
	print(ofTheJungle)
	ofTheJungle.sortByFitness()
	print(ofTheJungle)

testGenetics()
#testPopulation()
# testOutputNetwork()
