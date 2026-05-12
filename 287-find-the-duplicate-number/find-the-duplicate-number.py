class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # cycle detection
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = nums[0]
        fast = nums[fast]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
