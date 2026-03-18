class Solution:
    def findMin(self, nums: List[int]) -> int:
        # let's call the index where the array was rotated the kink
        # we're trying to find the kink, i.e., the smallest value
        # in this case, we perform binary search to explicitly look
        # at the unsorted part of the array. 
        # If the entire sub array is sorted, return the first index of the left side.
        
        # set our left and right indices
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2

            if nums[l] <= nums[mid] and nums[mid] <= nums[r]:
                return nums[l]
            # left side is sorted, look in the right side
            elif nums[l] <= nums[mid]:
                l = mid + 1
            # right side is sorted, look in the left side
            else:
                r = mid
        
        return nums[l]