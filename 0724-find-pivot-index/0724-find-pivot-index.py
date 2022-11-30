class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0;
        rightSum = sum(nums[0:])
        ind = 0;
        llist = len(nums)
        while (ind < llist) :
            rightSum -= nums[ind]
            if (leftSum == rightSum) :
                return ind 
            leftSum += nums[ind]
            ind += 1
        return -1
        