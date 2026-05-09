class Solution:
    def numDecodings(self, s: str) -> int:
        

        def numWays(ind, memo):  
            if ind in memo:
                return memo[ind]          
            if ind == len(s):
                memo[ind] = 1
                return 1
            if s[ind] == "0":
                memo[ind] = 0
                return 0
            # either take 1, or 2 values (if valid)
            res = numWays(ind+1, memo)
            if ind+1 < len(s):
                if s[ind] == "1" or s[ind] == "2" and s[ind+1] in "0123456":
                    res += numWays(ind+2, memo)
            memo[ind] = res
            return res

        return numWays(0, {})