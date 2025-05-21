class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        # i = 0
        # j = 1
        # while (i < j):
        #     if  nums[i] + nums[j] == target:
        #         return [i, j]
        #     if (j < len(nums)-1):
        #         j += 1
        #     else:
        #         i += 1
        #         j = i+1
        