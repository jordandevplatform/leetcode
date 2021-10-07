class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length=len(nums)
        shad=[]
        
        for i in range(length):
            for x in range (i+1,length):
                if nums[i] + nums[x] == target:
                    shad.append(i)
                    shad.append(x)
        return shad