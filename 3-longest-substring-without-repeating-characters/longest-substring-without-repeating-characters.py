class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edgecase: empty string
        if len(s) == 0:
            return 0
        # initialize pointers + hashmap for sliding window
        l = 0
        subLength = 0
        lastSeen = dict()
        for r in range(len(s)):
            val = lastSeen.get(s[r], None)
            if val != None:
                l = max(lastSeen[s[r]] + 1, l)
            lastSeen[s[r]] = r
            subLength = max(subLength, r - l + 1)
        return subLength
