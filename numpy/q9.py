import numpy as np
a=np.array([[10,20,30,40],
            [50,60,70,80],
            [90,100,110,120],
            [130,140,150,160]])

print("array :",a)
print("first row:",a[0])
print("last column",a[ :,-1])
print("diagonale ",np.diag(a))
print("2nd ",a[2])
print("3rd ",a[3])