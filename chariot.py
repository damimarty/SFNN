#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from genetics import Genetics
from network import Network

import random

class Chariot(object):
    def __init__(self):
        self.position = 0.00
        self.hasLoad = True
        self.fitness = -5.0
        self.contact = 1.0

    def reinit(self):
        if self.hasLoad:
            fitness = self.position
        else: fitness = 5.0 - self.position
        fitness += self.fitness
        self.position = 0.0
        self.hasLoad = True
        self.fitness = -5.0
        self.contact = 1.0
        return fitness if fitness > 0.1 else 0.1
        
    def run(self, inputArray, verbose = None):
        left = inputArray[0]
        right = inputArray[1]
        self.position += -left + right
        if self.position <=0.0:
            self.position = 0.0
            if not self.hasLoad:
                if verbose == True:
                    print "Got LOAD"
                self.contact = 1.0
                self.hasLoad = True
                self.fitness += 5.0
        if self.position >=5.0:
            self.position = 5.0
            if self.hasLoad:
                if verbose == True:
                    print "Left LOAD"
                self.contact = -1.0
                self.hasLoad = False
                self.fitness += 5.0
        # print self.position

        return [False]

    def getInputs(self):
        self.contact = self.contact * 0.55
        # self.contact = 0.0
        if self.position == 0.0:
            self.contact = 1.0
        if self.position == 5.0:
            self.contact = -1.0
        # return [1.0 if self.hasLoad else -1.0]
        # return [self.contact]
        return [5.0-self.position,self.position-5.0]
        
    

    def error(self,o1,o2):
        if (len(o1) == 1) and (len(o2) == 1):
            v = abs(o1[0] - o2[0])
            # return v**2
            return v
