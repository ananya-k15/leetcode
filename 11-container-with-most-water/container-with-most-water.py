class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        # use two pointers to traverse heights
        i, j = 0, len(height)-1

        while i < j:
            area = min(height[i], height[j]) * abs(i-j)
            maxArea = max(area, maxArea)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return maxArea
