#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from latchRS import latchRS
from network import Network
from genetics import Genetics

import matplotlib.pyplot as plt

def train():
	# Create our base Network
	pool = Genetics(genomes = [Network.recall()])
	pool.setProblem(latchRS())
	pool.train(100,50)

	"""
	if(pool.evolution):
		for speEvo in pool.evolution:
			plt.plot(speEvo)
	"""

	bestnn = pool.getBest()
	plt.figure()
	bestnn.draw()
	plt.show()
	bestnn.save("best.gen")

	plt.figure()
	plt.plot(pool.fitnesses)


train()

plt.show()
