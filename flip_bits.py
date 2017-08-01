def convert(value):
    notvalue=~value
    binarystring=str(bin(notvalue+2**32)[2:])
    decimal_value=int(binarystring,2)
    return decimal_value
number=int(input())
lists=[]
while number>0:
    value=int(input())
    lists.append(convert(value))
    number-=1

for value in lists:
    print(value)
