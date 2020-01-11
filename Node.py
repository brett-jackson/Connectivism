# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:23:05 2020
Generalized node class
@author: Brett
"""

class Node:
    def __init__(self,nid=None,value=None):
        self.nid = nid
        self.value = value
        self.outbound = {}
        self.inbound = {}
    def data(self):
        print('ID: ' + str(self.nid))
        print('Value: ' + str(self.value))
        print('Out: ' + str(self.outbound))
        print('In: ' + str(self.inbound))
        print()
    def __lt__(self,adjnode):
        typing = adjnode.__class__.__name__
        if typing=='Node':
            adjnode.outbound[str(self.nid)]=None
            self.inbound[str(adjnode.nid)]=None
        elif typing=='tuple':
            adjnode[0].outbound[str(self.nid)]=adjnode[1]
            self.inbound[str(adjnode[0].nid)]=adjnode[1]
    def __gt__(self,adjnode):
        typing = adjnode.__class__.__name__
        if typing=='Node':
            self.outbound[str(adjnode.nid)]=None
            adjnode.inbound[str(self.nid)]=None
        elif typing=='tuple':
            self.outbound[str(adjnode[0].nid)]=adjnode[1]
            adjnode[0].inbound[str(self.nid)]=adjnode[1]
        
        
if __name__ == '__main__':
    a = Node('a',1)
    b = Node('b',1)
    a<(b,1)
    a>(b,3)
    a.data()
    b.data()