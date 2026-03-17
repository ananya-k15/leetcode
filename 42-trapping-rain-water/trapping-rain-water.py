class Solution:
    def trap(self, height: List[int]) -> int:
        h = len(height)
        if h == 0:
            return h
        # compute the greatest value to the left and right of each index
        l = [0] * h
        for j in range(h-2, -1, -1):
            l[j] = max(l[j+1], height[j+1])
        r = [0] * h
        for i in range(1, h, 1):
            r[i] = max(height[i-1], r[i-1])

        water = 0
        for ind in range(h):
            diff = min(l[ind], r[ind]) - height[ind]
            if diff > 0:
                water += diff
        return water
        
