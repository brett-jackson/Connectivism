# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:25:17 2020
Self generating neural networks using Node class. 
Individual node must wait for all prior nodes to compute.
@author: Brett
"""
from Node import DirectedNode
from threading import Thread
import asyncio

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
        self.first = True
        self.semaFirst = asyncio.Semaphore()
        self.semaAll = asyncio.Semaphore(value=0)
    def forward(self):
        #Enter all threads
        #Set value in
        self.semaFirst.acquire() #decrement, starting at one
        if self.first: #First thread
            self.first = False
            self.semaFirst.release() #increment, allowing additional threads
            for inNode in range(len(self.inbound)):
                self.semaAll.acquire() #decrement and block until 
            #Calculate value
            self.value = self.act()
            #Forward nodes
        else: #Second and subsequent threads
            self.semaFirst.release()
            self.semaAll.release()
            return
            
            
        
#        for node in self.inbound:
            



