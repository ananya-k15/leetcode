from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m:
            return ""
        tcount = Counter(t)
        scount = Counter()
        minSubstring = ""
        if scount == tcount:
            return s[:n]
        l = 0
        for r in range(m):
            scount[s[r]] += 1
            # print(l, r, s[l:r])
            while tcount <= scount:
                # print(r-l-1, len(minSubstring))
                window = s[l:r+1]
                if not minSubstring or len(window) < len(minSubstring):
                    minSubstring = window
                scount[s[l]] -= 1
                if scount[s[l]] == 0:
                    del scount[s[l]]
                l += 1
        return minSubstring        