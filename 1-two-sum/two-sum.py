class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = dict()

        for x in range(len(nums)):
            if target-nums[x] in seen:
                return [seen[target-nums[x]], x]
            seen[nums[x]] = x
