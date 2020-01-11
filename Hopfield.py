# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:31:49 2020
Hopfield network using node objects.
@author: Brett
"""
from Node import UndirectedNode as UN

class Hopfield:
    def __init__(self,num):
        self.num = num
        self.weights = [0]*(num-1)*num/2