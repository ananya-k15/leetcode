class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a deque to store the index of the max element
        q = deque()
        results = []
        l, r = 0, 0 # to keep track of the sliding window
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # when the left pointer passes the max index stored in the queue
            # i.e., our max element index is outside the window now
            if l > q[0]:
                # we need to remove the max index
                q.popleft()
            # when we have a valid window
            if r-l+1 == k:
                # add the max for this window to the results array
                results.append(nums[q[0]])
                # move to the next window
                l += 1
            r += 1
        return results
