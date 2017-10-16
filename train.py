#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from latchRS import latchRS
from chariot import Chariot
from network import Network
from genetics import Genetics

import matplotlib.pyplot as plt

def train():
	# Create our base Network
<<<<<<< HEAD
	pool = Genetics(nbPeople = 70,genomes = [Network.recall()])
	pool.setProblem(latchRS())
	pool.train(nGenerations = 1000,nEvaluations=50)

	"""
	if(pool.evolution):
		for speEvo in pool.evolution:
			plt.plot(speEvo)
	"""

	plt.figure()
	plt.plot(pool.fitnesses)
=======
	pool = Genetics(nbPeople = 150, nbNeu = 15, nbConn = 40, nbNeuInput = 1, nbNeuOutput = 1)
	pool.setProblem(Chariot())

	char = 'y'
	fitnesses = []
	# while char == 'y':# char = raw_input("Continue ? (y or n)")
	fitnesses += pool.train(700,250)
		
	# if(pool.evolution):
		# for speEvo in pool.evolution:
			# plt.plot(speEvo)
>>>>>>> 05743ded6fbecf2da58bf49f988995e3d1639f78

	bestnn = pool.getBest()
	bestnn.save("best.gen")
	bestnn.printNetwork()
	testChariotOnBest(bestnn)
	plt.plot(pool.fitnesses)
	# plt.figure()
	# plt.plot(evolution)

def testChariotOnBest(bestNetwork):
	char = Chariot()
	route = []
	listinputsG = []
	listinputsD = []
	for i in range(100):
		inputs = char.getInputs()
		bestNetwork.setInput(inputs)
		bestNetwork.evaluateNetwork()
		commands = bestNetwork.getOutput()
		char.run(commands, verbose = False)
		print char.position
		route.append(char.position)
		listinputsG.append(inputs[0])
		# listinputsD.append(inputs[1])
	fit = char.reinit()
	print "fit = "+str(fit)
	plt.plot(route)
	plt.plot(listinputsG)
	# plt.plot(listinputsD)
	plt.figure()

	
train()

plt.show()
