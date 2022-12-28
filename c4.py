k=int(input("enter number of rows  =  "))
i,j,l=1,1,1
print(j)
print(l)
for i in range(1,k+1):
    for j in range(i):
        print(i,end=" ")
    
    for l in range(1,k+1-i):
        print("*",end=" ")
    j=1
    l=1
    print()






r=int(input("enter number of rows  = "))
c=int(input("enter number of columns  = "))

for i in range(r):
    for j in range(r-i):
        print("@",end="  ")
        
    print()
     
        







    n=int(input("enter the range =  "))
i=1
print("the numbers which arent multiples of 3,5,7 are=  ")
while i<n:
    if(i%3==0 or i%5==0 or i%7==0):
        pass
    else:    
      print(i,end="   ")
    i+=1




