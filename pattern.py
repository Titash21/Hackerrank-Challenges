lines=int(input())
j=lines
for i in range(0,lines):
    while (j-i)>0:
        print(" ",end="")
        j-=1
    k=i
    while(k>0):
        print("#",end="")
        k-=1
    print("")
