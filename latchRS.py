#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from genetics import Genetics

class latchRS(object):
    def __init__(self):
        output = 0.0
    def run(self, inputArray):
        iSet, iReset = inputArray
        if iSet == 1.0 and iReset == 0.0:
            self.output = 0.8
        if iSet == 0.0 and iReset == 1.0:
            self.output = 0.2
        if iSet == 1.0 and iReset == 1.0:
            if self.output == 0.8:
                self.output = 0.2
            else: self.output = 0.8

def testPool():
    latch = latchRS()
    base = Network(10, 10, 2, 1)
    baseGenome = base.getGenes()
    pool = Genetics(genome = baseGenome)
    # nb generation
    for age in range(100):
        for people in pool.peopleList:
            error = 0.0
            for i in range(100):
                iSet = 1.0 if random.random() > 0.9 else 0.0
                iReset = 1.0 if random.random() < 0.1 else 0.0
                inputArray = [iSet, iReset]
                expected = latch.run(inputArray)
                people.evaluateNetwork()
                error += abs(people.getOutput()[0]- expected)
            people.setFitness(1/error)
        pool.step()
