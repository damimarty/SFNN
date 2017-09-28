#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from genetics import Genetics
from network import Network
from math import sqrt
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
		return [self.output]

	def getInputs(self):
		iSet = 1.0 if random.random() > 0.9 else 0.0
		iReset = 1.0 if random.random() < 0.1 else 0.0
		return [iSet,iReset]

	def error(self,o1,o2):
		if (len(o1) == 1) and (len(o2) == 1):
			v = o1[0] - o2[0]
			return v**2


def train():
	# Create our base Network
	base = Network(10, 10, 2, 1)
	baseGenome = base.getGenes()
	pool = Genetics(genome = baseGenome)
	pool.setProblem(latchRS())
	pool.train(20,50)
	evolution = pool.computeEvolution()

	for speEvo in evolution:
		plt.plot(speEvo)

	plt.figure()
	plt.plot(pool.fitnesses)
	plt.show()

train()
