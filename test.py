#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from latchRS import latchRS
from network import Network

import matplotlib.pyplot as plt

def test():
	pb = latchRS()
	nn = Network(4, 5, 2, 1)
	for i in range(50):
		inputs = pb.getInputs()
		nn.setInput(inputs)
		nn.evaluateNetwork()
		o1 = pb.run(inputs)
		o2 = nn.getOutput()
		print(o1,o2)

def execLatch(name):
	bestPeople = Network(genes=Network.recall(name))
	tester = latchRS()
	a_inputR = []
	a_inputS = []
	a_expected = []
	a_output = []
	for i in range(250):
		inputArray = tester.getInputs()
		iSet, iReset = inputArray
		expected = tester.run(inputArray)
		a_inputR.append((iReset/5.0)-0.6)
		a_inputS.append((iSet/5.0)-0.3)
		a_expected.append(expected)
		bestPeople.setInput(inputArray)
		bestPeople.evaluateNetwork()
		a_output.append(bestPeople.getOutput())

	plt.plot(a_inputR[10:])
	plt.plot(a_inputS[10:])
	plt.plot(a_expected[10:])
	plt.figure()
	plt.plot(a_output[10:])

execLatch("best.gen")
plt.show()
