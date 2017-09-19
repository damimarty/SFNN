#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-
import math
import random
from timeit import default_timer as timer

class Connexion(object):
    def __init__(self, From = None, To = None, w = None):
        """blah"""
        self.From = From
        self.To = To
        if w is None: self.w = random.random()-0.5
        else: self.w = w

    def setW(self, w = None):
        if w is None: self.w = random.random()
        else: self.w = w

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
        self.sum = 0.0
        self.output = 0.0
        self.isInput = False
        self.isOutput = False
        
    def getOutput(self):
        return self.output
        
    def amIOutput(self):
        return self.isOutput
        
    def amIInput(self):
        return self.isInput
        
    def getId(self):
        return self.Id
        
    def updateSum(self, value):
        self.sum += value
        
    def compute(self):
        self.output = 1.0/(1.0+math.exp(-self.sum))
        self.sum = 0.0


class Network(object):
    def __init__(self, nbNeurons = 5, nbConnexions = 5):
        self.nbNeurons = 0
        self.neuronList = []
        self.nbConnexions = 0
        self.connexionList = []
        self.toggle = False
        # creating neurons
        for idNeuron in range(nbNeurons):
            self.createNeuron()

        # creating connexions
        for idConnexion in range(nbConnexions):
            self.createConnexion()
            
    def printNetwork(self):
        print "There are "+str(self.nbConnexions)+" connexions"
        for connexion in self.connexionList:
            print "I am a connexion and I link "+str(connexion.getFrom().getId()) + "\tto " + str(connexion.getTo().getId()) + "\twith a force " + str(connexion.getW())
        print "There are "+str(self.nbNeurons)+" neurons"
        for neuron in self.neuronList:
            print "I am a neuron, my name is "+str(neuron.getId()) +"\tand my output is ["+str(neuron.getOutput())+"]"
            
    def evaluateNetwork(self):
        for connexion in self.connexionList:
            connexion.getTo().updateSum(connexion.getFrom().getOutput() * connexion.getW())
        for neuron in self.neuronList:
            neuron.compute()

    def createConnexion(self):
        neuron1 = random.randint(0,nbNeurons-1)
        neuron2 = random.randint(0,nbNeurons-1)
        while self.neuronList[neuron1].amIOutput() : neuron1 = random.randint(0,nbNeurons-1)
        while self.neuronList[neuron2].amIInput() : neuron2 = random.randint(0,nbNeurons-1)
        self.connexionList.append(Connexion(self.neuronList[neuron1],self.neuronList[neuron2]))
        self.nbConnexions += 1
        
    def deleteConnexion(self, connexion):        
        self.connexionList.remove(connexion)
        self.nbConnexions -= 1
    
    def createNeuron(self):
        self.neuronList.append(Neuron(self.nbNeurons))
        self.nbNeurons += 1
        
    def deleteNeuron(self, neuron): 
        self.neuronList.remove(neuron)
        self.nbNeurons -= 1

nbNeurons = 5
nbConnexions = 8
george = Network(nbNeurons, nbConnexions)
george.evaluateNetwork()
# george.printNetwork()
start = timer()
for i in range(100):
    george.evaluateNetwork()
george.evaluateNetwork()
end = timer()
george.printNetwork()

print(end - start)  












