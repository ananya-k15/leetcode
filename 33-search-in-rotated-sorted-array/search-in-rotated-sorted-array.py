class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # edgecase: when nums only has one element
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        # use pointers at the ends of the arrays to do binary search
        l, r = 0, len(nums)-1
        while l <= r:
            # compute mid
            mid = (l+r)//2
            # did we find the target?
            if nums[mid] == target:
                return mid
            # find the sorted side of the array
            if nums[l] <= nums[mid]:
                # left side is sorted
                # check if the target lies in the sorted half
                if nums[l] <= target < nums[mid]:
                    # if so, look at the left side
                    r = mid - 1
                else:
                    # target must lie in the unsorted half,
                    # i.e., the right side of the array
                    l = mid + 1
            else:
                # right side is sorted
                # check if the target lies in the sorted half
                if nums[mid] < target <= nums[r]:
                    # if so, look at the right side
                    l = mid + 1
                else:
                    # target must lie in the unsorted half,
                    # i.e., the left side of the array
                    r = mid - 1
        # return -1 if target is not found.
        return -1