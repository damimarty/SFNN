#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from population import Population
from network import Network
import random
import matplotlib.pyplot as plt
import time
import numpy as np

defaultNbIndividuals = 5
defaultNbNeurons = 5
defaultNbConnexions = 8
class Genetics(object):
    def __init__(self, nbPeople = 100, nbNeu = 10, nbConn = 10, nbNeuInput = 2, nbNeuOutput = 1, genomes = None):
        self.pbaNewNeuron = 0.02
        self.pbaNewConnexion = 0.005
        self.pbaChangeConnexionLink = 0.01
        self.pbaChangeConnexionWeight = 0.05
        self.pbaDeleteNeuron = 0.01
        self.pbaDeleteConnexion = 0.03
        self.elitism = 2
        self.wheelSize = 0.0
        self.generation = 0

        # Our parent generation
        self.generationN = Population(nbPeople, nbNeu, nbConn, nbNeuInput, nbNeuOutput, genomes)
        # Our child generation
        self.generationNplusOne = Population(nbPeople, nbNeu, nbConn, nbNeuInput, nbNeuOutput, genomes)
        self.computeWheelSize()

        self.fitnesses = []
        self.speciesData = []
        self.individualSpecies = []

        self.problem = None
        # self.saveEvolution = False
        self.dicSpecies = {}
        self.initSpecies = []
        self.date = 0
        self.nbSpecies = []

    def setProblem(self,pb):
        self.problem = pb


    def train(self, nGenerations, nEvaluations):
        self.scenario = self.problem.getScenario(nEvaluations)
        if self.problem != None:
            # N generations
            for i in range(nGenerations):
                # Iterate over population
                self.do(nEvaluations, scenario)
                # Save genetics data of the current generation
                # if(self.saveEvolution):
                    # self.saveData()
                # Save fitness
                self.saveEvolution()
                best = self.saveFitness()
                # Do a genetic step
                self.step()
                # Copy child generation -> parent generation
                self.loop()
                print "Generation "+str(self.generation)+"\t"+str(best)
                # print("loop",time.time()-t)
                # print("next age : %d"%i)
                self.generation += 1
        else:
            print("no problem defined")
        return self.fitnesses

    def do(self,nEvaluations, scenario = None):
        identifierPeople = 0
        for nn in self.generationN.peopleList:
            # print "People "+str(identifierPeople)
            error = 0.0
            # Apply nEvaluations times our inputs
<<<<<<< HEAD
            #for j in range(nEvaluations):
            #    inputs = self.problem.getInputs()
            for inputs in self.scenario:
                o1 = self.problem.run(inputs)
                nn.setInput(inputs)
                nn.evaluateNetwork()
                o2 = nn.getOutput()
                error += self.problem.error(o2,o1)
            nn.setFitness(1/(error/nEvaluations))
=======
            if scenario is None:
                for j in range(nEvaluations):
                    inputs = self.problem.getInputs()
                    nn.setInput(inputs)
                    nn.evaluateNetwork()
                    commands = nn.getOutput()
                    self.problem.run(commands)
                    # error += self.problem.error(o2,o1)
            else:
                for j in range(len(scenario)):
                    inputs = scenario[j]
                    o1 = self.problem.run(inputs)
                    nn.setInput(inputs)
                    nn.evaluateNetwork()
                    o2 = nn.getOutput()
                    error += self.problem.error(o2,o1)
            fit = self.problem.reinit()
            # print fit
            nn.setFitness(fit)
            identifierPeople +=1
>>>>>>> 05743ded6fbecf2da58bf49f988995e3d1639f78

    def step(self):
        self.generationN.sortByFitness()
        self.computeWheelSize()
        self.generationNplusOne.clean()
        # copy best individuals
        self.generationNplusOne.extend(self.generationN.getFirsts(self.elitism))
        # fornicate the rest of population
        for i in range(self.generationN.size()-self.elitism):
            # print "Fornication n"+str(i)
            self.generationNplusOne.append(self.fornicate())

    def saveFitness(self):
        # Get the best fitnesses
        best = self.generationN.getBestFitness()
        self.fitnesses.append(best)
        return best

    def display(self):
        print self.fitnesses
        # plt.stackplot(self.fitnesses)
        plt.plot(self.fitnesses)
        # plt.figure()
        plt.show()

    def saveEvolution(self):
        # Get the best fitnesses
        self.fitnesses.append(self.generationN.getBestFitness())
        sp = self.getGenotypes()
        # print "There are "+str(len(sp))+" species in this generation"
        self.nbSpecies.append(str(len(sp)))
        # save the current spieces and counts
        # self.speciesData.append(sp)
        # check if new spiece born
        totalPeople = 0
        max_len = 0
        dicUpdated = {}
        for gsp,c in sp:
            # print str(c) + " type " + str(gsp)
            self.dicSpecies[gsp] = self.dicSpecies.get(gsp, self.initSpecies) + [c]
            max_len = len(self.dicSpecies[gsp])
            dicUpdated[gsp] = True
        for key in self.dicSpecies.keys():
            if key not in dicUpdated.keys():
                # print key
                # print "avt "+str(self.dicSpecies[key])
                self.dicSpecies[key] = self.dicSpecies.get(key, self.initSpecies) + [0]
                # print "apr "+str(self.dicSpecies[key])
            # if len(self.dicSpecies[key]) < self.date:
                # self.dicSpecies[gsp] = self.dicSpecies.get(gsp, self.initSpecies) + [0]
        self.initSpecies.append(0)
        self.date += 1
    def loop(self):
        self.generationN.setPopulation(self.generationNplusOne.getPopulation())

    def getBest(self):
        self.do(100)
        self.generationN.sortByFitness()
        return self.generationN.peopleList[0]

    def getSpieces(self):
        return self.generationN.getSpieces()

    def getGenotypes(self):
        return self.generationN.getGenotypes()

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
        while parent2 == parent1 or parent2 == None:
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
        child.clean()
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
        # connexion link
        if(self.yesOrNo(self.pbaChangeConnexionLink)):
            # print("mutateC")
            indexConnMutation = int(len(c)*random.random())
            src, dest, weight = c[indexConnMutation]
            c[indexConnMutation] = src, dest, random.random()
        # connexion weight
        if(self.yesOrNo(self.pbaChangeConnexionWeight)):
            # print("mutateN")
            indexConnMutation = int(len(c)*random.random())
            src, dest, weight = c[indexConnMutation]
            newConnIndex = int(len(n)*random.random())
            if(self.yesOrNo(0.5)):
                c[indexConnMutation] = newConnIndex, dest, weight
            else:
                c[indexConnMutation] = src, newConnIndex, weight
        # new connexion
        # if(self.yesOrNo(self.pbaNewConnexion)):
            # print("new Connexion")
            # neuron1 = random.randint(0,len(n)-1)
            # neuron2 = random.randint(0,len(n)-1)
            # tuple = neuron1, neuron2, random.random()
            # c.append(tuple)
        return n,c

    def computeEvolution(self):
        evolution = [[] for i in range(len(self.individualSpecies))]
        print(len(evolution))

        for data in self.speciesData:
            for g in self.individualSpecies:
                print g
                found = False
                for genome,count in data:
                    #print(genome,g)
                    if Network.isSameGenotype(genome,g):
                        found = True
                        evolution[self.individualSpecies.index(genome)].append(count)
                if not found:
                    evolution[self.individualSpecies.index(g)].append(0)
        return evolution
