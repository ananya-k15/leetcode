from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k, n = len(s1), len(s2) # our fixed window size
        if k > n:
            return False
        # create a counter to map char -> freq in s2
        s1count = Counter(s1)
        s2count = Counter(s2[:k])
        if s1count == s2count:
            return True
        for r in range(k, n):
            # s2count = Counter(s2[x:x+k])
            s2count[s2[r]] += 1
            s2count[s2[r-k]] -= 1
            if s2count[s2[r-k]] == 0:
                del s2count[s2[r-k]]
            if s1count == s2count:
                return True
        return False
