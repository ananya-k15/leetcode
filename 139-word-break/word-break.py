class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)

        def dp(ind, memo = None):
            if ind in memo:
                return memo[ind]

            if ind == n:
                memo[ind] = True
                return True
            
            for x in wordDict:
                if n-ind >= len(x) and s[ind:ind+len(x)] == x:
                    if dp(ind+len(x), memo):
                        memo[ind] = True
                        return True
            memo[ind] = False
            return False
        
        return dp(0, {})
