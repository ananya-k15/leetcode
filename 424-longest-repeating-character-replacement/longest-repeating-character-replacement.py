from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Use a sliding window
        l = 0
        maxSubLen = 0
        subString = Counter()
        maxFreq = 0

        for r in range(len(s)):
            # if condition is not met, shrink window from left
            subString[s[r]] += 1
            maxFreq = max(maxFreq, subString[s[r]])
            # print("At (", l, ", ", r, "subLen", subLen, "maxFreq", maxFreq, "and k", k)
            if (r - l + 1) - maxFreq > k:
                subString[s[l]] -= 1
                l += 1
            # print(r - l + 1, maxSubLen)
            maxSubLen = max(r - l + 1, maxSubLen)

        return maxSubLen