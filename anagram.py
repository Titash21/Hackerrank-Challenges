def calculate(string):
    lengths=len(string)
    if(lengths%2!=0):
        return -1
    else:
        change=0
        counter=0
        mid=lengths/2
        string1=string[:int(mid)]
        string2=string[int(mid):]
        while (counter<len(string1)):
            index=string2.find(string1[counter])
            if index!=-1:
                string2=string2[:index]+string2[index+1:]
                string1=string1[:counter]+string1[counter+1:]
                counter=0
            else:
                counter+=1
        change=len(string1)
        return change


test_cases=int(input())
answer=[]
while test_cases>0:
    strings=input()
    answer.append(calculate(strings))
    test_cases-=1

for value in answer:
    print(value)
