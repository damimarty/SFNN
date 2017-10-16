#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from latchRS import latchRS
from network import Network
from genetics import Genetics

import matplotlib.pyplot as plt

def train():
	# Create our base Network
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

	bestnn = pool.getBest()
	plt.figure()
	bestnn.draw("best")
	print(bestnn.fitness)
	plt.show()
	bestnn.save("best.gen")

train()

plt.show()
