class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in list(range(len(nums))):
            x=nums[i]
            for y in nums[i+1:]:
                if x+y==target:
                    return [nums.index(x),nums[i+1:].index(y)+i+1]

                
    