message = input().split()

d = int(input())
n = int(input())
strings=list()

for value in message:
    Decrypted=(int((value))**d)%n
    strings.append(chr(Decrypted))

str1 = ''.join(strings)
print(str1)
