size=int(input("size: "))
array=input("array: ").split()

negative=0
positive=0
zero=0
for number in array:
    if int(number)<0:
        negative+=1
    elif int(number)>0:
        positive+=1
    else:
        zero+=1

print(negative/size)
print(positive/size)
print(zero/size)
