class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0; right = 1
        while left >= 0 and right <= len(numbers): 
            current = numbers[left] + numbers[right]
            if current < target : 
                left += 1; right += 1
            elif current == target :
                return [left + 1, right + 1]
            else : 
                left -= 1    