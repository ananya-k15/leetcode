class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        end = len(nums)
        nums = sorted(nums)
        def backtrack(start, current):
            results.append(current[:])
            prev = None
            for ind in range(start, end):
                if nums[ind] == prev:
                    continue
                current.append(nums[ind])
                backtrack(ind+1, current)
                current.pop()
                prev = nums[ind]
        backtrack(0, [])
        return list(results)