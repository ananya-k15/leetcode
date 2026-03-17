class Solution:
    def trap(self, height: List[int]) -> int:
        h = len(height)
        # compute the greatest value to the left and right of each index
        l = [0] * h
        for j in range(h-2, -1, -1):
            l[j] = max(l[j+1], height[j+1])
        r = [0] * h
        for i in range(1, h, 1):
            r[i] = max(height[i-1], r[i-1])

        minVal = [min(l[x], r[x]) for x in range(h)]
        water = 0
        for ind in range(h):
            diff = minVal[ind] - height[ind]
            if diff > 0:
                water += diff
        return water
        
