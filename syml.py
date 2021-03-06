from numpy import *
from fractions import Fraction

B = mat([[0.5,0.5,-0.5],[0,0,0],[0.25,0.25,0.25]])
A = mat([[0.182721773, -0.000000000, 0.000000000],\
         [0.000000000, 0.182721773, 0.000000000],\
         [0.000000000, 0.000000000, 0.091673294]])
C = A*B
print(C)
a1 = ((C[0,0]-C[1,0])**2+(C[0,1]-C[1,1])**2+(C[0,2]-C[1,2])**2)**0.5
a2 = ((C[2,0]-C[1,0])**2+(C[2,1]-C[1,1])**2+(C[2,2]-C[1,2])**2)**0.5
print(a1,a2)
a = a1/a2
b = round(a,1)
print(b)
print(Fraction(b))