def decrypt(message,keys):
    new_message=[]
    i=0
    for char in message:
        if(ord(char)>=65 and ord(char)<=90):
            if(i<len(keys)):
                key=int(keys[i])
                new_message.append(chr(((ord(char) - 65 - key) % 26) + 65))
                i=i+1
            else:
                i=0
                key=int(keys[i])
                new_message.append(chr(((ord(char) - 65 - key) % 26) + 65))
                i=i+1
        elif(ord(char)>=97 and ord(char)<=122):
            if(i<len(keys)):
                key=int(keys[i])
                new_message.append(chr(((ord(char) - 97 - key) % 26) + 97))
                i=i+1
            else:
                i=0
                key=int(keys[i])
                new_message.append(chr(((ord(char) - 97 + key) % 26) + 97))
                i=i+1
        else:
            new_message.append(char)

    encrypted=''.join(new_message)
    return encrypted


def find_key(encrypted):
    Emessage=encrypted[-20:]
    Amessage="-Your friend, Alice"
    int_key=[]
    for Achar,Echar in zip(Amessage,Emessage):
        if(ord(Achar)>=65 and ord(Achar)<=90):
            #straight appending
            if(ord(Achar)-ord(Echar)<=0):
                int_key.append(abs(ord(Achar)-ord(Echar)))
            #overflow
            else:
                int_key.append(abs((26-(ord(Achar)-ord(Echar)))))

        elif((ord(Achar)>=97 and ord(Achar)<=122)):
            if(ord(Achar)-ord(Echar)<=0):
                int_key.append(abs(ord(Achar)-ord(Echar)))
            else:
                int_key.append(abs((26-(ord(Achar)-ord(Echar)))))

    key=''.join(str(x) for x in int_key)
    return key



def encrypt(message,keys):
    new_message=[]
    i=0
    for char in message:
        if(ord(char)>=65 and ord(char)<=90):
            if(i<len(keys)):
                key=int(keys[i])
                new_message.append(chr(((ord(char) - 65 + key) % 26) + 65))
                i=i+1
            else:
                i=0
                key=int(keys[i])
                new_message.append(chr(((ord(char) - 65 + key) % 26) + 65))
                i=i+1
        elif(ord(char)>=97 and ord(char)<=122):
            if(i<len(keys)):
                key=int(keys[i])
                new_message.append(chr(((ord(char) - 97 + key) % 26) + 97))
                i=i+1
            else:
                i=0
                key=int(keys[i])
                new_message.append(chr(((ord(char) - 97 + key) % 26) + 97))
                i=i+1
        else:
            new_message.append(char)

    encrypted=''.join(new_message)
    return encrypted

def main():

    message=input("enter your message: ")
    key=input("enter your key: ")
    result=encrypt(message,key)
    print("encrypted message is: ",result)
    keys=find_key(result)
    print("keys",keys)
    message=decrypt(result,keys)
    print(message)
    
main()
