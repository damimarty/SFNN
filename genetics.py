#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from population import Population
import random

defaultNbIndividuals = 5
defaultNbNeurons = 5
defaultNbConnexions = 8
class Genetics(object):
    def __init__(self, populationN = None):
        self.pbaNewNeuron = 0.02
        self.pbaNewConnexion = 0.05
        self.pbaDeleteNeuron = 0.01
        self.pbaDeleteConnexion = 0.03
        self.elitism = 2
        self.wheelSize = 0.0
        if populationN is None:
            self.generationN = Population(defaultNbIndividuals,defaultNbNeurons,defaultNbConnexions)
        else: self.generationN = populationN
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
                return self.generationN.peopleList[index]
            threshold += fit
        return None

    def getParents(self):
        parent1 = self.drawLot()
        parent2 = self.drawLot()
        while parent2 == parent1:
            print "same"
            parent2 = self.drawLot()
        return parent1, parent2

    #def step(self):
        #for i in range(self.elitism):
            #copy best individuals
        #for individual in self.generationN.peopleList:
        #self.generationNplusOne.extend(self.generation.peopleList)
        #parent1, parent2 = self.getParents()
        #child = self.fornication(parent1, parent2)

    def fornication(self, parent1, parent2):
        neurons1, connexions1 = parent1.getGenes()
        neurons2, connexions2 = parent2.getGenes()
        split = int(random.random()*len(neurons1))
        neuronsChild = neurons1[0:split]
        neuronsChild.extend(neurons2[split:])
        split = int(random.random()*len(connexions1))
        connexionsChild = connexions1[0:split]
        connexionsChild.extend(connexions2[split:])


ofTheJungle = Population(4, 2, 2)
print(ofTheJungle)
ofTheJungle.sortByFitness()
print(ofTheJungle)

pool = Genetics()
pool.getGenerationN(ofTheJungle)
parent1, parent2 = pool.getParents()
pool.fornication(parent1, parent2)
print parent1, parent2
