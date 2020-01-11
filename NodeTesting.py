# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:27:05 2020
Testing script for node class.
@author: Brett
"""

from Node import DirectedNode as DN, UndirectedNode as UN

### TEST DIRECTED NODE ###
A = DN('A', 1)
B = DN('B', 2)
# No weights
A > B
B > A
A.data()
B.data()

# With weights
A > (B, 5)
B > (A, 3)
A.data()
B.data()

### TEST UNDIRECTED NODE ###
C = UN('A', 1)
D = UN('B', 2)
# No weights
C == D
C.data()
D.data()

# With weights
C == (D, 5)
C.data()
D.data()