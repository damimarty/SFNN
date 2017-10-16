#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

import random
import math

class Neuron(object):
	def __init__(self, id = -1, bias = None):
		"""blah"""
		self.Id = id
		self.sum = 0.0
		if bias:
			self.bias = bias
		else:
			self.bias = random.random()
		self.output = random.random()

	def getOutput(self):
		return self.output

	def getId(self):
		return self.Id

	def updateSum(self, value):
		self.sum += value

	def compute(self):
		if sum < -20.0:
			self.output = 1.0
		else:
			self.output = (1.0/(1.0+math.exp(-self.sum)))*2.0-1.0
		self.sum = 0.0

class InputNeuron(Neuron):
	def __init__(self, id = -1, bias = None):
		Neuron.__init__(self,id,bias)

	def setInput(self, inputValue):
		# coerce to [1:0] ?
		self.sum = inputValue

	def updateSum(self, value):
		pass

	def compute(self):
		self.output = self.sum

class OutputNeuron(Neuron):

	def __init__(self, id = -1, bias = None):
		Neuron.__init__(self,id,bias)
		self.isOutput = True

	def getOutput(self):
		return self.output
