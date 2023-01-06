import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 : return True
        news = ''.join(l for l in s if l.isalnum()).lower()
        w = len(news) // 2
        if len(news) % 2 == 0 :
            return news[:w] == news[:w-1:-1]
        else : 
            return news[:w] == news[:w:-1]
        # return news == news[::-1] 