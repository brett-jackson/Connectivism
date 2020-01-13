# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:27:05 2020
Testing script for node class.
@author: Brett
"""

from Node import DirectedNode as DN, UndirectedNode as UN

### TEST DIRECTED NODE ###
print("\n####################################\n####################################\nDIRECTED NODE TESTS\n####################################\n####################################\n")
A = DN('A', 1)
B = DN('B', 2)
C = DN('C', 3)
D = DN('D', 4)
E = DN('E', 5)
F = DN('F', 6)
G = DN('G', 7)
H = DN('H', 8)
I = DN('I', 9)
J = DN('J', 10)

# No weights
print("\n####################################\nNo weights\n####################################\n")
print("A = DN('A', 1)")
print("B = DN('B', 2)")
print("A >> B")
print("B >> A")
A >> B
B >> A
A.data()
B.data()

# With weights
print("\n####################################\nWith weights\n####################################\n")
print("C = DN('C', 3)")
print("D = DN('D', 4)")
print("C >> (D, 5)")
print("D >> (C, 3)")
C >> (D, 5)
D >> (C, 3)
C.data()
D.data()

# With list
print("\n####################################\nWith list\n####################################\n")
print("E = DN('E', 5)")
print("F = DN('F', 6)")
print("G = DN('G', 7)")
print("E >> [F,G]")
print("E << [(F,1),(G,2)]")
E >> [F,G]
E << [(F,1),(G,2)]
E.data()
F.data()
G.data()

# With chaining
print("\n####################################\nWith chaining\n####################################\n")
print("H = DN('H', 8)")
print("I = DN('I', 9)")
print("J = DN('J', 10)")
print("H>>(I,1)<<(J,2)")
H>>(I,1)<<(J,2)
H.data()
I.data()
J.data()

### TEST UNDIRECTED NODE ###
print("\n####################################\n####################################\nUNDIRECTED NODE TESTS\n####################################\n####################################\n")

A = UN('A', 1)
B = UN('B', 2)
C = UN('C', 3)
D = UN('D', 4)
E = UN('E', 5)
F = UN('F', 6)
G = UN('G', 7)
H = UN('H', 8)
I = UN('I', 9)
J = UN('J', 10)
# No weights
print("\n####################################\nNo weights\n####################################\n")
print("A = UN('A', 1)")
print("B = UN('B', 2)")
print("A | B")
A | B
A.data()
B.data()

# With weights
print("\n####################################\nWith weights\n####################################\n")
print("C = UN('C', 3)")
print("D = UN('D', 4)")
print("C | (D, 5)")
C | (D, 5)
C.data()
D.data()

# With list
print("\n####################################\nWith list\n####################################\n")
print("E = UN('E', 5)")
print("F = UN('F', 6)")
print("G = UN('G', 7)")
print("E | [(F, 5), G]")
E | [(F, 5), G]
E.data()
F.data()
G.data()

# With chaining
print("\n####################################\nWith chaining\n####################################\n")
print("H = UN('H', 8)")
print("I = UN('I', 9)")
print("J = UN('J', 10)")
print("H|(I,1)|(J,2)")
H|(I,1)|(J,2)
H.data()
I.data()
J.data()
