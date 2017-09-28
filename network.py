#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from connexion import Connexion
from neuron import Neuron
from neuron import InputNeuron
from neuron import OutputNeuron

import pygraphviz as pgv

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import random
import math

import pickle

class Network(object):

	def __init__(self, nbNeurons = 5, nbConnexions = 5, nbInputsNeurons = 2, nbOutputsNeurons = 1, genes = None):
		self.fitness = 0.0
		if(genes != None):
			neuronGenes = genes[0]
			connexionGenes = genes[1]
			# print(neuronGenes)
			# print(connexionGenes)
			self.nbNeurons = 0
			self.neuronList = []
			self.inputNeuronList = []
			self.outputNeuronList= []
			self.connexionList = []
			for neuronGene in neuronGenes:
				neuron = None
				if neuronGene[1] == 'n':
					neuron = Neuron(self.nbNeurons,bias=neuronGene[0])
				elif neuronGene[1] == 'i':
					neuron = InputNeuron(self.nbNeurons,bias=neuronGene[0])
					self.inputNeuronList.append(neuron)
				elif neuronGene[1] == 'o':
					neuron = OutputNeuron(self.nbNeurons,bias=neuronGene[0])
					self.outputNeuronList.append(neuron)
				self.neuronList.append(neuron)
				self.nbNeurons += 1
			for connGene in connexionGenes:
				fromNeuron = self.neuronList[connGene[0]]
				toNeuron = self.neuronList[connGene[1]]
				self.connexionList.append(Connexion(fromNeuron,toNeuron,connGene[2]))
			self.nbConnexions = len(self.connexionList)
			self.species = str(self.nbNeurons)+"_"+str(self.nbConnexions)
		else:
			self.nbNeurons = 0
			self.neuronList = []
			self.inputNeuronList = []
			self.outputNeuronList= []
			self.nbConnexions = 0
			self.connexionList = []
			self.species = str(self.nbNeurons)+"_"+str(self.nbConnexions)
			for idInputNeuron in range(nbInputsNeurons):
				self.createNeuron("input")
			for idNeuron in range(nbNeurons-nbInputsNeurons-nbOutputsNeurons):
				self.createNeuron()
			for idOutputNeuron in range(nbOutputsNeurons):
				self.createNeuron("output")
			for idConnexion in range(nbConnexions):
				self.createConnexion()

	def isSame(self,other):
		return self.isSameGenome(self.getGenes(),other.getGenes())

	@staticmethod
	def isSameGenome((n1,c1),(n2,c2)):
		# neurons
		same = True
		for nelem1,nelem2 in zip(n1,n2):
			if((nelem1[0] != nelem2[0]) or (nelem1[1] != nelem2[1])):
				same = False
		# connexions
		for nelem1,nelem2 in zip(c1,c2):
			if((nelem1[0] != nelem2[0]) or (nelem1[1] != nelem2[1]) or (nelem1[2] != nelem2[2])):
				same = False
		return same

	def getNeuronPosition(self, neuron):
		return self.neuronList.index(neuron)

	def sortedConnexions(self):
		sortedConnexionList = []
		for connex in self.connexionList:
			indexFrom = self.getNeuronPosition(connex.getFrom())
			indexTo = self.getNeuronPosition(connex.getTo())
			sortedConnexionList.append(Connexion(indexFrom,indexTo,connex.getW()))
		sortedConnexionList = sorted(sortedConnexionList, key = lambda c: (c.getFrom(), c.getTo()))
		return sortedConnexionList

	def getGenes(self):
		genesNeurons = []
		genesConnexions = []
		for n in self.neuronList:
			t = "n"
			if type(n) is InputNeuron:
				t = "i"
			elif type(n) is OutputNeuron:
				t = "o"
			genesNeurons.append((n.bias,t))
		for c in self.sortedConnexions():
			genesConnexions.append((c.getFrom(),c.getTo(),c.getW()))
		return genesNeurons, genesConnexions

	def printNetwork(self):
		print "My species is "+self.species
		print "There are "+str(self.nbConnexions)+" connexions"
		for connexion in self.connexionList:
			print connexion
		print "There are "+str(self.nbNeurons)+" neurons"
		for neuron in self.neuronList:
			print "I am a neuron, my name is "+str(neuron.getId()) +"\tand my output is ["+str(neuron.getOutput())+"]"

	def setInput(self, inputArray):
		if(len(inputArray) == len(self.inputNeuronList)) :
			for inputScalar,inputNeuron in zip(inputArray,self.inputNeuronList):
				inputNeuron.setInput(inputScalar)
		else:
			print("input size array does not match network input size")


	def getOutput(self):
		outputs = []
		for neuron in self.outputNeuronList:
			outputs.append(neuron.getOutput())
		return outputs


	def evaluateNetwork(self):
		for connexion in self.connexionList:
			connexion.getTo().updateSum(connexion.getFrom().getOutput() * connexion.getW())
		for neuron in self.neuronList:
			neuron.compute()

	def extractNeuronsOutputs(self):
	    r = []
	    for neuron in self.neuronList:
	        r.append(neuron.getOutput())
	    return r

	def createConnexion(self):
		neuron1 = random.randint(0,self.nbNeurons-1)
		neuron2 = random.randint(0,self.nbNeurons-1)
		# this is not forbidden to imagine getting a feedback on how much the network controls some output,
		# so next line is commented
		# while self.neuronList[neuron1].amIOutput() : neuron1 = random.randint(0,nbNeurons-1)
		#while self.neuronList[neuron2].amIInput() : neuron2 = random.randint(0,nbNeurons-1)
		self.connexionList.append(Connexion(self.neuronList[neuron1],self.neuronList[neuron2]))
		self.nbConnexions += 1

	def deleteConnexion(self, connexion):
		self.connexionList.remove(connexion)
		self.nbConnexions -= 1

	def createNeuron(self, type = "norm"):
		if type == "input":
			neuron = InputNeuron(self.nbNeurons)
			self.neuronList.append(neuron)
			self.inputNeuronList.append(neuron)
		elif type == "output":
			neuron = OutputNeuron(self.nbNeurons)
			self.neuronList.append(neuron)
			self.outputNeuronList.append(neuron)
		else:
			neuron = Neuron(self.nbNeurons)
			self.neuronList.append(neuron)
		self.nbNeurons += 1

	def deleteNeuron(self, neuron):
		self.neuronList.remove(neuron)
		if neuron in self.inputNeuronList:
			self.inputNeuronList.remove(neuron)
		if neuron in self.outputNeuronList:
			self.outputNeuronList.remove(neuron)
		self.nbNeurons -= 1

	def setFitness(self, fitness):
		self.fitness = fitness

	def getFitness(self):
		return self.fitness

	def draw(self):

		self.g = pgv.AGraph(directed=True)

		for node in self.neuronList:
			color = "white"
			if type(node) is OutputNeuron:
				color = "red"
			elif type(node) is InputNeuron:
				color = "blue"
			print(node.Id,color)
			self.g.add_node(str(node.Id),style="filled",fillcolor=color)

		for conn in self.connexionList:
			f = str(conn.From.Id)
			t = str(conn.To.Id)
			self.g.add_edge(f,t,arrowhead="normal",arrowsize=1.0,color="red",penwidth=(conn.w+1)*2)

		print(self.g.string())
		self.g.write('net.dot')

		gFile=pgv.AGraph('net.dot') # create a new graph from file
		gFile.layout() # layout with default (neato)
		gFile.draw('net.png') # draw png

		img=mpimg.imread('net.png')
		imgplot = plt.imshow(img)

		#plt.show()

	def save(self,name):
		genome = self.getGenes()
		pickle.dump( genome, open(name, "wb" ))

	@staticmethod
	def recall(name = "master.gen"):
		return pickle.load(open(name, "rb" ) )
