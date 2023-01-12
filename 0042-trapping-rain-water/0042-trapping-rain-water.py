class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1 : 
            return 0
        water = 0; left = [0]; right = [0]
        maxLeft = height[0]; maxRight = height[-1]
        for i in range(len(height) - 1) :
            maxLeft = max(maxLeft, height[i])
            left.append(maxLeft)
        for j in range(len(height)-1, 0, -1) :
            maxRight = max(maxRight, height[j])
            right.append(maxRight)
        right = right[::-1]
        # print(left, right)
        for x in range(len(height)) : 
            water += max(min(left[x], right[x]) - height[x], 0)
        return water