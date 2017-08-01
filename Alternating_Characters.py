test_cases=input("enter the test cases: ")
strings=input("enter the strings: ").split()
WrongList=[]
for word in strings:
    length=len(word)
    i=0
    #Checks all strings not alternate
    while i<length-1:
        #if the string is not fine
        if word[i]==word[i+1]:
            WrongList.append(word)
            break
        i+=1

print("wrong list : " ,WrongList)
newList=[]
for words in WrongList:
    length=len(words)
    i=0
    while i<length-1:
        if words[i]==words[i+1]:
            words=words[:i+1]+words[i+2:]
            i=0
            length=len(words)
            continue
        i+=1
    newList.append(words)

print("New List: ", newList)

for word in strings:
    difference=
