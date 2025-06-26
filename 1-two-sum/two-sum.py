class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        seen[nums[0]] = 0

        for i in range(1, len(nums), 1):
            val = target - nums[i]
            if val in seen.keys():
                return [i, seen[val]]
            seen[nums[i]] = i

        return -1