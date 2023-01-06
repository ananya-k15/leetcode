class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0; right = len(numbers) - 1
        while True: 
            current = numbers[left] + numbers[right]
            if current < target : 
                left += 1
            elif current == target :
                return [left + 1, right + 1]
            else : 
                right -= 1 