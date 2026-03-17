class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        results = []

        # sort the list to get the non decreasing order of elements
        nums.sort()

        for i in range(len(nums)):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # to get to target, we need to find j and k s.t.
            # nums[k] + nums[j] == -nums[i]
            # if nums[i] < 0, look on the right hand side
            # if nums[i] > 0, all the remaining numbers are positive 
            # so we can skip this (we would have already found a possible combo)
            if nums[i] > 0:
                break
            
            j, k = i+1, len(nums)-1
            while j < k:
                total = nums[j] + nums[k] + nums[i]
                if total == 0:
                    results.append([nums[i], nums[j], nums[k]])

                    # Skip duplicates for j
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    # Skip duplicates for k
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

                    j += 1
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        # res = [list(x) for x in results]
        return results