
n=int(input("enter the range =  "))
from numpy import *
ar=array('i'ones(n))
print(ar)
for i in range(n):
    x=ar[i]+i
    ar[i]=x
ar=ar*2
ar2=array([1,22,3,4])
ar3=ar2+ar

print(ar3)
print(concatenate([ar,ar3,ar2]))
print(sum(concatenate([ar,ar3,ar2])))
ar4=array([1,22,3,44,6,7])
ar5=copy(ar4)
print(ar4)
print(ar5)
print(id(ar4))
print(id(ar5))

from numpy import *
ar=linspace(0,9,20)
ar2=arange(1,15,2,float)
ar3=ones(5,int)

print(ar2)
print(ar3)
print(ar)

