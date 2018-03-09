import time

def romanToInt( s):
    """
    :type s: str
    :rtype: int
    """
    print("Roman Number:", s,end=" ")
    diction = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    reduced = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    num = 0
    for key, value in reduced.items():
        count=0
        while (key in s):
            num += reduced[key]
            index=s.find(key)
            s=s[0:index]+s[index+len(key):]


    for key,value in diction.items():
        while (key in s):
            num += diction[key]
            index = s.find(key)
            s = s[0:index] + s[index + len(key):]

    print("Integer Number:",num)

start_time = time.time()
romanToInt("XIVIV")
end = time.time()
print(end-start_time, "seconds")
romanToInt("MCMXCVI")

def romanToIntSmarter(s):
    #Say we have a number --
    # 1. XV, reverse it VX by default they are in increasing order ie d[V]<d[V] then we can directly add the values
    # 2. Say XIVIV , reverse it we get VIVIX
    # 3. Now the least roman number is I, so p is initialized to I
    # 4. What happens is if they do not follow the increasing order trend, that means they have smaller strings
    # 5. Keep comparing and updating values of p, if it violates the trend, substract it from the total res

    d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    res, p = 0, 'I'
    for c in s[::-1]:
        res, p = res - d[c] if d[c] < d[p] else res + d[c], c
    return res

start_time = time.time()
print("Integer is:",romanToIntSmarter("XIVIV"))
end = time.time()
print(end - start_time, "seconds")
print("Integer is:",romanToInt("MCMXCVI"))