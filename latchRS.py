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
        iReset = 1.0 if random.random() < 0.05 else 0.0
        return [iSet,iReset]

    def error(self,o1,o2):
        if (len(o1) == 1) and (len(o2) == 1):
            v = abs(o1[0] - o2[0])
            # return v**2
            return v


def train1():
		# Create our base Network
		genomes = []
		for i in range(5):
			g = Network(10, 10, 2, 1)
			genomes.append(g.getGenes())
		pool = Genetics(genomes = genomes)
		pool.setProblem(latchRS())
		pool.train(500,50)
		return (pool.computeEvolution(),pool.fitnesses)

	evolution, fitness = train()

	if(evolution):
		for speEvo in evolution:
			plt.plot(speEvo)
	plt.figure()
	plt.plot(fitness)
	plt.show()

def train2()
    # Create our base Network
    base = Network(7, 10, 2, 1)
    base.printNetwork()
    baseGenome = base.getGenes()
    pool = Genetics(genome = baseGenome)
    pool.setProblem(latchRS())
    pool.train(200,75)
    # evolution = pool.computeEvolution()

    bestPeople = pool.generationN.getFirsts(1)[0]
    bestPeople.printNetwork()
    print bestPeople.fitness

    # for speEvo in evolution:
        # plt.plot(speEvo)

    # plt.figure()
    # plt.plot(pool.fitnesses)
    # plt.figure()

    tester = latchRS()
    a_inputR = []
    a_inputS = []
    a_expected = []
    a_output = []
    for i in range(250):
        inputArray = tester.getInputs()
        iSet, iReset = inputArray
        expected = tester.run(inputArray)
        a_inputR.append((iReset/5.0)-0.6)
        a_inputS.append((iSet/5.0)-0.3)
        a_expected.append(expected)
        bestPeople.setInput(inputArray)
        bestPeople.evaluateNetwork()
        a_output.append(bestPeople.getOutput())
    plt.plot(a_inputR)
    plt.plot(a_inputS)
    plt.plot(a_expected)
    plt.figure()
    plt.plot(a_output)

train()
