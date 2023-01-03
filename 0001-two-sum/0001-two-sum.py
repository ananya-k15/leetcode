class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2 : 
            return [0, 1]
        # for i in range(len(nums)) :
        #     left = target - nums[i]
        #     # for j in range(i + 1, len(nums), 1) : 
        #     #     if nums[j] == left : return [i, j]
        #     if left in nums[i+1:] :
        #         return [i, i + 1 + nums[i+1:].index(left)]
        dnums = dict()
        for i in range(len(nums)) : 
            left = target - nums[i]
            if left in dnums.keys() : 
                return [i, dnums.get(left)]
            else : 
                dnums[nums[i]] = i
        
        