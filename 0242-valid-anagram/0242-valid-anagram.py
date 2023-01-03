class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        strack, ttrack = dict(), dict()
        for i in range(0, len(s), 1) :
            strack[s[i]] = 1 + strack.get(s[i], 0)
            ttrack[t[i]] = 1 + ttrack.get(t[i], 0)
        return strack == ttrack