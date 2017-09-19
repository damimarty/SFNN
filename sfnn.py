# -*- Python -*-
# -*- coding: latin-1 -*-
import math
import random

class Connexion(object):
    def __init__(self, From = -1, To = -1, w = 0.0):
        """blah"""
        self.From = From
        self.To = To
        self.w = w

    def setW(self, w):
        self.w = w

    def getW(self):
        return self.w
        
    def setFrom(self, From):
        self.From = From
        
    def setTo(self, To):
        self.To = To
        
    def getFrom(self):
        return self.From
        
    def getTo(self):
        return self.To
        
class Neuron(object):
    def __init__(self, id = -1):
        """blah"""
        self.Id = id
        self.sum = 0.1
        self.output = 0.0
        
    def getOutput(self):
        return self.output
        
    def getId(self):
        return self.Id
        
    def updateSum(self, value):
        self.sum += value
        
    def compute(self):
        print self.sum
        self.output = 1.0/(1.0+math.exp(-5.0*self.sum))
        self.sum = 0.0


class Network(object):
    def __init__(self, nbNeurons = 5, nbConnexions = 5):
        self.nbNeurons = nbNeurons
        self.neuronList = []
        self.nbConnexions = nbConnexions
        self.connexionList = []
        self.toggle = False
        # creating neurons
        for idNeuron in range(nbNeurons):
            self.neuronList.append(Neuron(idNeuron))

        # creating connexions
        for idConnexion in range(nbConnexions):
            neuron1 = random.randint(0,nbNeurons-1)
            neuron2 = random.randint(0,nbNeurons-1)
            #
            # while neuron1 == neuron2:
                # neuron2 = random.randint(0,nbNeurons-1)
            #
            self.connexionList.append(Connexion(neuron1,neuron2,random.random()))
            
    def printNetwork(self):
        for connexion in self.connexionList:
            print "I am a connexion and I link "+str(connexion.getFrom()) + " to " + str(connexion.getTo()) + " with a force " + str(connexion.getW())
        for neuron in self.neuronList:
            print "I am a neuron, my name is "+str(neuron.getId()) +" and my output is ["+str(neuron.getOutput())+"]"
            
    def evaluateNetwork(self):
        print "\nEvaluating...\n"
        for connexion in self.connexionList:
            self.neuronList[connexion.getTo()].updateSum(self.neuronList[connexion.getFrom()].getOutput() * connexion.getW())
        for neuron in self.neuronList:
            neuron.compute()

    # def updateConnexion(self):
    # def createConnexion(self):
    # def deleteConnexion(self):
    # def createNeuron(self):
    # def deleteNeuron(self):


george = Network(15, 30)
george.printNetwork()
george.evaluateNetwork()
george.evaluateNetwork()
george.printNetwork()












