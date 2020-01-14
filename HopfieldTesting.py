# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:42:19 2020
Testing for hopfield nets
@author: Brett
"""
from Hopfield import Hopfield
hop = Hopfield(9)
hop.hebbLearn([[-1,1,1,
                -1,1,1,
                -1,1,1],
                [1,1,-1,
                 1,1,-1,
                 1,1,-1]])
hop.forward([-1,1,1,
             -1,1,1,
             1,1,-1])

