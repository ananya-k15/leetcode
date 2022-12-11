class Solution:
    def isPalindrome(self, x: int) -> bool:
        # all negative numbers are automatically not palindromes
        if x < 0 :
            return False
        
        # for all positive integers
        forward = str(x)
        backward = forward[::-1] 
        if forward == backward : return True
        return False