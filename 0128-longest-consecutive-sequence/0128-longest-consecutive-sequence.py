class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == [] : return 0
        nums.sort()
        longest = 1; i = 1; long = 1
        while i < len(nums) :
            if nums[i] - nums[i-1] == 1 :
                long += 1
            elif nums[i] - nums[i-1] != 0 : 
                if longest < long : longest = long
                long = 1
            i += 1
        if longest < long : longest = long
        return longest