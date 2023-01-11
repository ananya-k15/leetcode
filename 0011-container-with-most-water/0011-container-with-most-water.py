class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0; right = width = len(height) - 1
        maxProd = width * min(height[left], height[right])
        while left < right : 
            if height[left] < height[right] : 
                left += 1; width -= 1
            elif height[right] < height[left] : 
                right -= 1; width -= 1
            else :
                left += 1; right -= 1; width -= 2
            prod = width * min(height[left], height[right])
            maxProd = max(prod, maxProd)
        return maxProd