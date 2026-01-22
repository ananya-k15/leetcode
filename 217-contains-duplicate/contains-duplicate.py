class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # edge case: if nums has length == 1
        if len(nums) == 1:
            return False
        # otherwise
        else:
            # create a hashmap hash_nums
            hash_nums = set()
            # loop over every element in the array
            for x in nums:
                # check if it exists in a hashmap
                if x in hash_nums:
                    # if it does, then return true
                    return True
                else:
                    # if it doesn't, then add it to hashmap and continue
                    hash_nums.add(x)
        
        # if the loop ends and we haven't found a duplicate, return False
        return False