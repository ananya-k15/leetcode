class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        results = []
        def backtrack(start, current):
            if start == n:
                results.append(current[:])
            for x in range(start, n+1):
                sub = s[start:x]
                if sub != "" and sub == sub[::-1]:
                    current.append(sub)
                    backtrack(x, current)
                    current.pop()              
        backtrack(0, [])
        return results