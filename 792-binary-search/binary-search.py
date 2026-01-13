class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)

        # loop runs while the index range is valid
        while left < right:
            # at each step, calculate a mid index
            mid = (left + right) // 2
            # if mid == target, return mid
            if nums[mid] == target:
                return mid
            # if mid > target, discard the bigger half
            elif nums[mid] > target:
                right = mid
            # if mid < target, discard the smaller half
            else:
                left = mid+1
                
        # if loop finishes without returning, we couldn't find a solution, return -1
        return -1