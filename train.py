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
	# pool = Genetics(genomes = [Network.recall()])
	pool = Genetics(nbPeople = 150, nbNeu = 8, nbConn = 15, nbNeuInput = 1, nbNeuOutput = 1)
	pool.setProblem(Chariot())
	# scenario = pool.problem.getScenario(500)
	# pool.train(500,50,scenario)
	char = 'y'
	fitnesses = []
	while char == 'y':
		fitnesses += pool.train(5,300)
		char = raw_input("Continue ? (y or n)")

	"""
	if(pool.evolution):
		for speEvo in pool.evolution:
			plt.plot(speEvo)
	"""

	bestnn = pool.getBest()
	# evolution = pool.computeEvolution()
	# plt.figure()
	# bestnn.draw()
	# plt.show()
	bestnn.save("best.gen")
	bestnn.printNetwork()
	testChariotOnBest(bestnn)
	# plt.figure()
	plt.plot(pool.fitnesses)
	# plt.plot(fitnesses)
	# plt.figure()
	# plt.plot(evolution)

def testChariotOnBest(bestNetwork):
	char = Chariot()
	route = []
	listinputs = []
	for i in range(100):
		inputs = char.getInputs()
		bestNetwork.setInput(inputs)
		bestNetwork.evaluateNetwork()
		commands = bestNetwork.getOutput()
		char.run(commands, verbose = False)
		# print char.position
		route.append(char.position)
		listinputs.append(inputs[0])
	fit = char.reinit()
	print "fit = "+str(fit)
	bestNetwork.printNetwork()
	bestNetwork.clean()
	bestNetwork.printNetwork()
	plt.plot(route)
	plt.plot(listinputs)
	plt.figure()

def testChariot():
	char = Chariot()
	left = 0.0
	right = 0.5
	for i in range(2):
		char.run([0.0,0.5], verbose = True)
		# print char.position
	# for i in range(50):
		# char.run([0.5,0.0], verbose = True)
		# print char.position
	# for i in range(50):
		# char.run([0.0,0.5], verbose = True)
		# print char.position
	fit = char.reinit()
	print fit
	
	
	
train()
# testChariot()

plt.show()
