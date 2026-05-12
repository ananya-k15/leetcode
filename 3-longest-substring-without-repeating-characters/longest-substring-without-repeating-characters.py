class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        # abcabcbb
        longest = 0 # 
        i, j = 0, 0
        substring = deque([s[i]]) # a, b
        while j < len(s): # 0 < 8
            longest = max(longest, len(substring))
            while s[j] in substring:
                substring.popleft()
            substring.append(s[j])
            j += 1
        longest = max(longest, len(substring))
        return longest