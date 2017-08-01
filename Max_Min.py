# Enter your code here. Read input from STDIN. Print output to STDOUT
numbers=input()
number_list1=[int(x) for x in numbers.split()]
number_list2=[int(x) for x in numbers.split()]

i=0
sum_max=0
sum_min=0

while i<4:
    sum_max+=max(number_list1)
    sum_min+=min(number_list2)
    number_list1.remove(max(number_list1))
    number_list2.remove(min(number_list2))
    i+=1
print(sum_min, sum_max)

    
