#!/usr/bin/python
# -*- Python -*-
# -*- coding: latin-1 -*-

from latchRS import latchRS
from chariot import Chariot
from network import Network
from genetics import Genetics

import numpy as np
import matplotlib.pyplot as plt
import Tkinter as tk
import wx
import sys
import GUI.noname as noname

def train2():
    return True
    
def createPool(nbPeople, nbNeu, nbConn, problem):
    nbNeuInput, nbNeuOutput = problem.getIOspec()
    pool = Genetics(nbPeople, nbNeu, nbConn, nbNeuInput, nbNeuOutput)
    pool.setProblem(problem)
    
    return pool
def train(pool, nbGeneration = None):
    if nbGeneration is None:
        nbGeneration = 150
    print "Running "+str(nbGeneration)
    nbRun = 0
    char = 'y'
    # while char == 'y':
        # fitnesses = []
    fitnesses = pool.train(nbGeneration,250)
    nbRun += nbGeneration
        # char = raw_input("Continue ? (y or n)")
    
    # bestnn = pool.getBest()
    # bestnn.save("best.gen")
    # bestnn.printNetwork()
    plt.plot(pool.nbSpecies)
    plt.figure()

    twoDarray = []
    bigTuple = ()
    for key in pool.dicSpecies.keys():
        tempList = pool.dicSpecies[key]
        bigTuple = bigTuple + (tempList,)
    twoDarray = np.vstack(bigTuple)
    plt.stackplot(range(0, len(tempList)),twoDarray)
    plt.show()

def display(pool):
    pool.display()

class CalcFrame(noname.MyFrame1): 
    def __init__(self,parent): 
        noname.MyFrame1.__init__(self,parent) 
        
    def setPool(self, pool):
        self.pool = pool
        
    def run1Generation(self,event): 
        train(self.pool, 1)
        # train(1)
        
    def run100Generation(self,event): 
        train(self.pool, 150)
        # train(100)
        
    def displayFitnesses(self,event):
        display(self.pool)


if __name__ == '__main__':
    # pool creation
    pool = createPool(150, 15, 40, Chariot())
    app = wx.App(False) 
    frame = CalcFrame(None) 
    frame.setPool(pool) 
    frame.Show(True) 
    #start the applications 
    app.MainLoop() 
