#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from population import Population
from network import Network
import random
import matplotlib.pyplot as plt
defaultNbIndividuals = 5
defaultNbNeurons = 5
defaultNbConnexions = 8
class Genetics(object):
    def __init__(self, nbPeople, nbNeu, nbConn, nbNeuInput, nbNeuOutput):
        self.pbaNewNeuron = 0.02
        self.pbaNewConnexion = 0.05
        self.pbaDeleteNeuron = 0.01
        self.pbaDeleteConnexion = 0.03
        self.elitism = 2
        self.wheelSize = 0.0
        self.generationN = Population(nbPeople, nbNeu, nbConn, nbNeuInput, nbNeuOutput)
        self.computeWheelSize()
        self.generationNplusOne = None

    def computeWheelSize(self):
        for people in self.generationN.peopleList:
            self.wheelSize += people.getFitness()

    def drawLot(self):
        parent = None
        threshold = 0.0
        lot = random.random()*self.wheelSize
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
        child = Network(genes = (neuronsChild,connexionsChild))
        return child
