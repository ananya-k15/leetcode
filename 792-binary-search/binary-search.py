class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def search_index(nums, left, right, target):
            # check whether there are any elements in the provided range
            if right <= left:
                return -1
            # if yes, compute middle index
            else:
                m = (left + right) // 2
                if target == nums[m]:
                    return m
                elif target < nums[m]:
                    return search_index(nums, left, m, target)
                else:
                    return search_index(nums, m+1, right, target)
        
        return search_index(nums, 0, len(nums), target)
            