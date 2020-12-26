#bubble sorting in ascending order
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]<nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

nums=[5,47,8,9,45,4687,35435,786765,45378,765,
      435,4,
      357,53756,454,23432,757,534531,23753,745]
sort(nums)
print(nums)
