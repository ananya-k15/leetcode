class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for i in nums :
            numset.add(i)
        if len(nums) == len(numset) :
            return False
        return True
        