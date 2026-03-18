class Solution:
    def isHappy(self, n: int) -> bool:
        
        # declare a hashset to store all numbers 
        # discovered while computing sum of squares
        seen = set()
        num = n

        # loop until we either hit one or a number in seen
        while True:
            prodSum = 0
            while num > 0:
                prodSum += (num % 10)**2
                num = int(num // 10)
            if prodSum == 1:
                return True
            if prodSum in seen:
                return False
            seen.add(prodSum)
            num = prodSum
        return False