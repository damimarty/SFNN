#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from population import Population
from network import Network
import random
import matplotlib.pyplot as plt
import time

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

        # Our parent generation
        self.generationN = Population(nbPeople, nbNeu, nbConn, nbNeuInput, nbNeuOutput, genome)
        # Our child generation
        self.generationNplusOne = Population(nbPeople, nbNeu, nbConn, nbNeuInput, nbNeuOutput, genome)
        self.computeWheelSize()

        self.fitnesses = []
        self.speciesData = []
        self.individualSpecies = []

        self.problem = None

    def setProblem(self,pb):
        self.problem = pb

    def train(self, nGenerations, nEvaluations):
        if self.problem != None:
            # N generations
            for i in range(nGenerations):
                # Iterate over population
                t = time.time()
                for nn in self.generationN.peopleList:
                    error = 0.0
                    inputs = self.problem.getInputs()
                    # Apply nEvaluations times our inputs
                    for j in range(nEvaluations):
                        o1 = self.problem.run(inputs)
                        nn.setInput(inputs)
                        nn.evaluateNetwork()
                        o2 = nn.getOutput()
                        error += self.problem.error(o2,o1)
                    nn.setFitness(1/(1+(error/nEvaluations)))
                print("eval",time.time()-t)
                # Save genetics data of the current generation
                t = time.time()
                self.saveData()
                print("save",time.time()-t)
                # Do a genetic step
                t = time.time()
                self.step()
                print("step",time.time()-t)
                # Copy child generation -> parent generation
                t = time.time()
                self.loop()
                print("loop",time.time()-t)
                print("next age : %d"%i)
        else:
            print("no problem defined")

    def step(self):
        self.generationN.sortByFitness()
        self.computeWheelSize()
        self.generationNplusOne.clean()
        # copy best individuals
        self.generationNplusOne.extend(self.generationN.getFirsts(self.elitism))
        # fornicate the rest of population
        for i in range(self.generationN.size()-self.elitism):
            self.generationNplusOne.append(self.fornicate())

    def saveData(self):
        # Get the best fitnesses
        self.fitnesses.append(self.generationN.getBestFitness())
        sp = self.getSpieces()
        # save the current spieces and counts
        self.speciesData.append(sp)
        # check if new spiece born
        for gsp,c in sp:
            found = False
            for iSpecies in self.individualSpecies:
                if Network.isSameGenome(iSpecies,gsp):
                    found = True
                    break
            if not found:
                self.individualSpecies.append(gsp)

    def loop(self):
        self.generationN.setPopulation(self.generationNplusOne.getPopulation())

    def getSpieces(self):
        return self.generationN.getSpieces()

    def computeWheelSize(self):
        self.wheelSize = 0.0
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

    def computeEvolution(self):
        evolution = [[] for i in range(len(self.individualSpecies))]
        print(len(evolution))

        for data in self.speciesData:
            for g in self.individualSpecies:
                found = False
                for genome,count in data:
                    #print(genome,g)
                    if Network.isSameGenome(genome,g):
                        found = True
                        evolution[self.individualSpecies.index(genome)].append(count)
                if not found:
                    evolution[self.individualSpecies.index(g)].append(0)
        return evolution
