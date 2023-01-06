import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 : return True
        news = ''.join(l for l in s if l.isalnum()).lower()
        return news == news[::-1] 