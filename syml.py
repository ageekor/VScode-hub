from numpy import *

B = mat([[0.5,0.5,0.5],[0,0,0],[0.5,0,0.5]])
A = mat([[0.245397809 ,-0.141680491, -0.100183236],[0.000000000 , 0.283360982, -0.100183236],[0.000000000 , 0.000000000 , 0.300549708]])
C = A*B
print(C)
a1 = ((C[0,0]-C[1,0])**2+(C[0,1]-C[1,1])**2+(C[0,2]-C[1,2])**2)**0.5
a2 = ((C[2,0]-C[1,0])**2+(C[2,1]-C[1,1])**2+(C[2,2]-C[1,2])**2)**0.5
print(a1,a2)
print(a1/a2)