class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2 : 
            return [0, 1]
        for i in range(len(nums)) :
            left = target - nums[i]
            for j in range(i + 1, len(nums), 1) : 
                if nums[j] == left : return [i, j]
        
        