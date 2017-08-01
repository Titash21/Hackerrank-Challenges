# Enter your code here. Read input from STDIN. Print output to STDOUT
string=input()
count=1
for s in string:
    if ord(s)>=65 and ord(s)<=90:
        count+=1

print(count)
