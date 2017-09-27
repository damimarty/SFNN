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
    def __init__(self, nbPeople = 100, nbNeu = 10, nbConn = 10, nbNeuInput = 2, nbNeuOutput = 1, genome = None):
        self.pbaNewNeuron = 0.02
        self.pbaNewConnexion = 0.05
        self.pbaChangeConnexion = 0.05
        self.pbaDeleteNeuron = 0.01
        self.pbaDeleteConnexion = 0.03
        self.elitism = 2
        self.wheelSize = 0.0
        self.generationN = Population(nbPeople, nbNeu, nbConn, nbNeuInput, nbNeuOutput, genome)
        self.generationNplusOne = Population(nbPeople, nbNeu, nbConn, nbNeuInput, nbNeuOutput, genome)
        self.computeWheelSize()


    def step(self):
        self.generationN.sortByFitness()
        self.generationNplusOne.clean()
        #copy best individuals
        self.generationNplusOne.extend(self.generationN.getFirsts(self.elitism))
        for i in range(self.generationN.size()-self.elitism):
            self.generationNplusOne.append(self.fornicate())

    def loop(self):
        self.generationN.setPopulation(self.generationNplusOne.getPopulation())

    def getSpieces(self):
        return self.generationN.getSpieces()

    def computeWheelSize(self):
        for people in self.generationN.peopleList:
            self.wheelSize += people.getFitness()

    def yesOrNo(self,prob):
        return random.random() < prob

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

    def fornicate(self):
        p1,p2 = self.getParents()
        return self.fornication(p1,p2)

    def fornication(self, parent1, parent2):
        neurons1, connexions1 = parent1.getGenes()
        neurons2, connexions2 = parent2.getGenes()
        split = int(random.random()*len(neurons1))
        neuronsChild = neurons1[0:split]
        neuronsChild.extend(neurons2[split:])
        split = int(random.random()*len(connexions1))
        connexionsChild = connexions1[0:split]
        connexionsChild.extend(connexions2[split:])
        # Mutation part
        if(self.yesOrNo(self.pbaChangeConnexion)):
            indexConnMutation = int(len(connexionsChild)*random.random())
            src, dest, weight = connexionsChild[indexConnMutation]
            connexionsChild[indexConnMutation] = src, dest, random.random()
            child = Network(genes = (neuronsChild,connexionsChild))
        else:
            child = Network(genes = (neuronsChild,connexionsChild))
        return child
