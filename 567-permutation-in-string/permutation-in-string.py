from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k, n = len(s1), len(s2) # our fixed window size
        if k > n:
            return False
        # create a counter to map char -> freq in s2
        s1count = Counter(s1)
        for x in range(0, n-k+1, 1):
            s2count = Counter(s2[x:x+k])
            if s1count == s2count:
                return True

        return False
