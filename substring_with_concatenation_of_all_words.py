def words():
    word=[]
    string=input("enter the concatenated string: ")
    string_concat=""
    word_Size=int(input("Enter length of word array: "))
    for i in range(word_Size):
        string1=input("enter string: ")
        string_concat+=string1
        word.append(string1)
    reversed_string_concat=""
    for i in reversed(range(word_Size)):
        reversed_string_concat=reversed_string_concat+word[i]
    print(word, string_concat, string,reversed_string_concat)


    #find the first index of the correct order string and remove it from the string
    index1=string.find(string_concat)
    if(index1!=-1):
        print(index1)
    string=string.replace(string_concat,"",1)

    #find the first index of the reversed order string and remove it from the string

    index2=string.find(reversed_string_concat)
    if(index2!=-1):
        print(index2)
    string=string.replace(reversed_string_concat,"",1)

    #keep finding more occurences
    while(index1!=-1 or index2!=-1):
        index2=string.find(reversed_string_concat)
        index1=string.find(string_concat)
        if(index1!=-1):
            print(index1)
            string=string.replace(string_concat,"",1)
        if(index2!=-1):
            print(index2)
            string=string.replace(reversed_string_concat,"",1)






words()
