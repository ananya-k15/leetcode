class Solution:
    def partitionString(self, s: str) -> int:

        # max space complexity = n
        # time complexity = n
        
        num = 0
        seen = set()
        ind = 0
        while ind < len(s):
            if s[ind] in seen:
                num += 1
                seen = set()
            seen.add(s[ind])
            ind += 1
        
        return num+1