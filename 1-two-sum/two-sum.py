class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range (1,len(nums)):
                if (nums[i] + nums [j]) == target and i != j:
                    return [i,j]
        # i, j = 0, 1
        # while (i < j):
        #     if  nums[i] + nums[j] == target:
        #         return [i, j]
            
        #     if (j < len(nums)-1):
        #         j += 1
        #     else:
        #         i += 1
        
        # return result
        