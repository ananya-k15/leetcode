class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # traverse from back of the list
        num = 1
        for d in range(len(digits)-1, -1, -1):
            digits[d] += num
            if digits[d] > 9:
                num = digits[d] // 10
                digits[d] = int(digits[d] % 10)
            else:
                num = 0
                break
        if num != 0:
            digits = [num] + digits
        return digits
