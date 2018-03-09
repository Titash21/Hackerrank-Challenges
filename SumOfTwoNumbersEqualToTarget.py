def twoSum( nums, target):
    for i in range(len(nums)):
         if(target-nums[i] in nums[i+1:]):
            diff=target-nums[i]
            nums[i]='a'
            return [i, nums.index(diff) ]

print("Case 1",twoSum([6,3,3,7],6))
print("Case 2" ,twoSum([1,2,4,0],2))