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
    def __init__(self, nbPeople = 100, nbNeu = 10, nbConn = 10, nbNeuInput = 2, nbNeuOutput = 1, genomes = None):
        self.pbaNewNeuron = 0.02
        self.pbaNewConnexion = 0.05
        self.pbaChangeConnexionLink = 0.05
        self.pbaChangeConnexionWeight = 0.05
        self.pbaDeleteNeuron = 0.01
        self.pbaDeleteConnexion = 0.03
        self.elitism = 5
        self.wheelSize = 0.0

        self.bestSavedFitness = 0.0

        # Our parent generation
        self.generationN = Population(nbPeople, nbNeu, nbConn, nbNeuInput, nbNeuOutput, genomes)
        # Our child generation
        self.generationNplusOne = Population(nbPeople, nbNeu, nbConn, nbNeuInput, nbNeuOutput, genomes)
        self.computeWheelSize()

        self.fitnesses = []
        self.speciesData = []
        self.individualSpecies = []

        self.problem = None
        self.saveEvolution = False

    def setProblem(self,pb):
        self.problem = pb

    def train(self, nGenerations, nEvaluations):
        if self.problem != None:
            # N generations
            for i in range(nGenerations):
                # Iterate over population
                # t = time.time()
                self.do(nEvaluations)
                # print("eval",time.time()-t)
                # Save genetics data of the current generation
                if(self.saveEvolution):
                    # t = time.time()
                    self.saveData()
                    # print("save",time.time()-t)
                # Save fitness
                self.saveFitness()
                # Do a genetic step
                # t = time.time()
                self.step()
                # print("step",time.time()-t)
                # Copy child generation -> parent generation
                # t = time.time()
                self.loop()
                # print("loop",time.time()-t)
                print("next age : %d (%f)"%(i,self.getBest().fitness))
        else:
            print("no problem defined")

    def do(self,nEvaluations):
        for nn in self.generationN.peopleList:
            error = 0.0
            # Apply nEvaluations times our inputs
            for j in range(nEvaluations):
                inputs = self.problem.getInputs()
                o1 = self.problem.run(inputs)
                nn.setInput(inputs)
                nn.evaluateNetwork()
                o2 = nn.getOutput()
                error += self.problem.error(o2,o1)
            nn.setFitness(1/(error/nEvaluations))

    def step(self):
        self.generationN.sortByFitness()
        nn = self.generationN.peopleList[0]
        if(nn.fitness > self.bestSavedFitness):
            self.bestSavedFitness = nn.fitness
            nn.save("bests/superBest%d.gen"%self.bestSavedFitness)
            nn.draw("bests/superBest%d"%self.bestSavedFitness)
        self.computeWheelSize()
        self.generationNplusOne.clean()
        # copy best individuals
        self.generationNplusOne.extend(self.generationN.getFirsts(self.elitism))
        # fornicate the rest of population
        for i in range(self.generationN.size()-self.elitism):
            self.generationNplusOne.append(self.fornicate())

    def saveFitness(self):
        # Get the best fitnesses
        self.fitnesses.append(self.generationN.getBestFitness())

    def saveEvolution(self):
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

    def getBest(self):
        self.do(100)
        self.generationN.sortByFitness()
        # print([p.getFitness() for p in self.generationN.peopleList])
        return self.generationN.peopleList[0]

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
        # CrossOver
        neuronsChild,connexionsChild =  self.crossOver(parent1.getGenes(),parent2.getGenes())
        # Mutation part
        neuronsChild,connexionsChild =  self.mutate((neuronsChild,connexionsChild))
        child = Network(genes = (neuronsChild,connexionsChild))
        return child

    def crossOver(self,(n1,c1),(n2,c2)):
        split = int(random.random()*len(n1))
        neuronsChild = n1[0:split]
        neuronsChild.extend(n2[split:])
        split = int(random.random()*len(c1))
        connexionsChild = c1[0:split]
        connexionsChild.extend(c2[split:])
        return neuronsChild,connexionsChild

    def mutate(self,(n,c)):
        # connexion weight
        if(self.yesOrNo(self.pbaChangeConnexionLink)):
            # print("mutateC")
            indexConnMutation = int(len(c)*random.random())
            src, dest, weight = c[indexConnMutation]
            c[indexConnMutation] = src, dest, random.random()
        if(self.yesOrNo(self.pbaChangeConnexionWeight)):
            # print("mutateN")
            indexConnMutation = int(len(c)*random.random())
            src, dest, weight = c[indexConnMutation]
            newConnIndex = int(len(n)*random.random())
            if(self.yesOrNo(0.5)):
                c[indexConnMutation] = newConnIndex, dest, weight
            else:
                c[indexConnMutation] = src, newConnIndex, weight
        return n,c

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
