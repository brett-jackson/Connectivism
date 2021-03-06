# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:23:05 2020
Generalized node class supporting both undirected and directed graphs.
@author: Brett
"""

class Node:
    def __init__(self,nid=0,value=0):
        self.nid = nid
        self.value = value
        
    def data(self):
        print()
        print('ID: ' + str(self.nid))
        print('Value: ' + str(self.value))
    def setVal(self,val):
        self.value = val
        
class DirectedNode(Node):
    def __init__(self,nid=0,value=0):
        super().__init__(nid,value)
        self.outbound = {}
        self.inbound = {}
    def data(self):
        super().data()
        print('Out: ' + str(self.outbound))
        print('In: ' + str(self.inbound))
        print()
    def __lshift__(self,adjnode):
        typing = adjnode.__class__.__name__
        if typing=='DirectedNode':
            adjnode.outbound[str(self.nid)]=None
            self.inbound[str(adjnode.nid)]=None
            return adjnode
        elif typing=='tuple':
            adjnode[0].outbound[str(self.nid)]=adjnode[1]
            self.inbound[str(adjnode[0].nid)]=adjnode[1]
            return adjnode[0]
        elif typing=='list':
            for node in adjnode:
                self<<node
    def __rshift__(self,adjnode):
        typing = adjnode.__class__.__name__
        if typing=='DirectedNode':
            self.outbound[str(adjnode.nid)]=None
            adjnode.inbound[str(self.nid)]=None
            return adjnode
        elif typing=='tuple':
            self.outbound[str(adjnode[0].nid)]=adjnode[1]
            adjnode[0].inbound[str(self.nid)]=adjnode[1]
            return adjnode[0]
        elif typing=='list':
            for node in adjnode:
                self>>node
            
class UndirectedNode(Node):
    def __init__(self,nid=0,value=0):
        super().__init__(nid,value)
        self.adjacent = {}
    def data(self):
        super().data()
        print('Connections: ' + str(self.adjacent))
        print()
    def __or__(self,adjnode):
        typing = adjnode.__class__.__name__
        if typing=='UndirectedNode':
            adjnode.adjacent[str(self.nid)]=None
            self.adjacent[str(adjnode.nid)]=None
            return adjnode
        elif typing=='tuple':
            adjnode[0].adjacent[str(self.nid)]=adjnode[1]
            self.adjacent[str(adjnode[0].nid)]=adjnode[1]
            return adjnode[0]
        elif typing=='list':
            for node in adjnode:
                self|node
        
        