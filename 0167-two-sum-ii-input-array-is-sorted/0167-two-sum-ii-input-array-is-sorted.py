class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0; r = len(numbers) - 1
        while True: 
            current = numbers[l] + numbers[r]
            if current == target : 
                return [l + 1, r + 1]
            elif current < target :
                l += 1
            else : 
                r -= 1 