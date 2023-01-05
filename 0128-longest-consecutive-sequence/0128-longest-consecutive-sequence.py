class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for i in numset : 
            if i - 1 not in numset : 
                long = 1
                while i + long in numset : 
                    long += 1
                longest = max(longest, long)
        return longest