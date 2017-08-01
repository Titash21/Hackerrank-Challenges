# Enter your code here. Read input from STDIN. Print output to STDOUT
candles=input()
height_of_each_candle=input()
heights=[int(x) for x in height_of_each_candle.split()]
max=0
for value in heights:
    if value>max:
        max=value

sum=0
for value in heights:
    if value==max:
        sum+=1

print(sum)

#Solution 2
candles=input()
height_of_each_candle=input()
heights=[int(x) for x in height_of_each_candle.split()]

print(heights.count(((max(heights)))))
