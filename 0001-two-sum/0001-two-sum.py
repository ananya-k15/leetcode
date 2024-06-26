class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind, cval in enumerate(nums) :
            val = target - cval
            if val in hashmap :
                return sorted([ind, hashmap[val]])
            else : 
                hashmap[cval] = ind