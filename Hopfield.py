# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:31:49 2020
Hopfield network using node objects.
@author: Brett
"""
from Node import UndirectedNode as UN
from random import uniform
class Hopfield:
    def __init__(self,num):
        self.size = num
        self.weights = [0]*int((num-1)*num/2)
        for index,weight in enumerate(self.weights):
            self.weights[index] = uniform(-1,1)
        self.nodes = []
        for i in range(0,self.size):
            self.nodes+=[UN(i,0)]
            [self.nodes[i]|(self.nodes[j],self.weights[int((i-1)*i/2+j)]) for j in range(i)]
    def summary(self):
         for node in self.nodes:
             node.data()
        
        
