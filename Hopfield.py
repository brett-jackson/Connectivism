# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:31:49 2020
Hopfield network using node objects.
@author: Brett
"""
from Node import UndirectedNode as UN

class Hopfield:
    def __init__(self,num,lr=0.1):
        self.numPatterns = 0
        self.lr = lr
        self.size = num
        weights = [0]*int((num-1)*num/2) #initial weights
        self.threshold = 0
#        for index,weight in enumerate(weights):
#            weights[index] = uniform(-1,1)
        self.nodes = []
        for i in range(0,self.size):
            self.nodes+=[UN(i,0)]
            [self.nodes[i]|(self.nodes[j],weights[int((i-1)*i/2+j)]) for j in range(i)]
    def summary(self):
         print([node.value for node in self.nodes])
         print("Energy:" + str(self.energy()))
    def energy(self):
        energy = 0
        for node in self.nodes:
            energy+=self.threshold*node.value
            energy+=-0.5*sum([node.adjacent[key]*node.value*self.nodes[int(key)].value for key in node.adjacent])
        return energy
    def update(self,node):
        check = sum([node.adjacent[key]*self.nodes[int(key)].value for key in node.adjacent])
        lastVal = node.value
        if check >= self.threshold:
            node.setVal(1)
        else:
            node.setVal(-1)
        return lastVal == node.value
    def updateAsynch(self):
        changes = [False]*self.size
        while False in changes:
            self.summary()
            for node in self.nodes:
                changes[node.nid]=self.update(node)
    def setVals(self,vals):
        for index,node in enumerate(self.nodes):
            node.setVal(vals[index])
    def hebbLearn(self,patterns):
        if patterns[0].__class__.__name__ == 'list':
            self.numPatterns+=len(patterns)
        else:
            self.numPatterns+=1
            patterns = [patterns]
        n = self.numPatterns
        for p in range(n):
            self.setVals(patterns[p])
            for node in self.nodes:
                for adj in node.adjacent:
                    node.adjacent[adj]+=(1/n)*node.value*self.nodes[int(adj)].value
    def storkeyLearn(self,patterns):
        if patterns[0].__class__.__name__ == 'list':
            self.numPatterns+=len(patterns)
        else:
            self.numPatterns+=1
            patterns = [patterns]
        n = self.numPatterns
        for p in range(n):
            self.setVals(patterns[p])
            unchanged = self.nodes.copy()
            for index,node in enumerate(self.nodes):
                prev = unchanged[index]
                for adj in node.adjacent:
                    second = self.nodes[int(adj)] #Connected node
                    prev_second = unchanged[int(adj)]
                    field_node = sum([prev.adjacent[k]*unchanged[int(k)].value for k in prev.adjacent if k is not adj])
                    field_sec  = sum([prev_second.adjacent[k]*unchanged[int(k)].value for k in prev_second.adjacent if int(k) is not index])
                    node.adjacent[adj]+=prev.adjacent[adj]+(1/n)*(node.value*second.value-node.value*field_sec-second.value*field_node)
    def forward(self,start,n=1):
        self.setVals(start)
        self.updateAsynch()
        
