#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from population import Population
import random

class Genetics(object):
    def __init__(self):
        self.pbaNewNeuron = 0.02
        self.pbaNewConnexion = 0.05
        self.pbaDeleteNeuron = 0.01
        self.pbaDeleteConnexion = 0.03
        self.elitism = 2
        self.wheelSize = 0.0
        self.generationN = None
        self.generationNplusOne = None

    def getGenerationN(self, populationN):
        self.generationN = populationN
        for index in range(len(populationN.peopleList)):
            self.wheelSize += populationN.peopleList[index].getFitness()

    def drawLot(self):
        parent = None
        threshold = 0.0
        lot = random.random()*self.wheelSize
        print lot
        for index in range(len(self.generationN.peopleList)):
            fit = self.generationN.peopleList[index].getFitness()
            if  fit + threshold > lot:
                return index
            threshold += fit
        return None

    def getParents(self):
        parent1 = self.drawLot()
        parent2 = self.drawLot()
        while parent2 == parent1:
            print "same"
            parent2 = self.drawLot()
        return parent1, parent2

    def createNewGeneration(self):
        parent1, parent2 = self.getParents()
        child = fornication(parent1, parent2)


ofTheJungle = Population(4, 2, 2)
print(ofTheJungle)
ofTheJungle.sortByFitness()
print(ofTheJungle)

pool = Genetics()
pool.getGenerationN(ofTheJungle)
parent1, parent2 = pool.getParents()
print parent1, parent2
