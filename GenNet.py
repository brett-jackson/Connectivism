# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:25:17 2020
Self generating neural networks using Node class. 
@author: Brett
"""
from Node import DirectedNode

class GenNode(DirectedNode):
    def __init__(self,actFunction,nid=0,value=0):
        super().__init__(nid,value)
        self.inVar = 0   #High input variance -> higher breadth
        self.inMean = 0
        self.inCount = 0
        self.backVar = 0 #High backprop variance -> higher depth
        self.backMean = 0
        self.backCount = 0
        self.act = actFunction
    
    def forward():
        inVal = 0
        for node in self.inbound:
            



