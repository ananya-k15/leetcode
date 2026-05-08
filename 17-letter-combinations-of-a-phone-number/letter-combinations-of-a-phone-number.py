class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        letMap = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"
        }

        results = []
        n = len(digits)

        def backtrack(ind, current):
            if len(current) == n:
                results.append(current)
                return
            if ind >= n:
                return
            for ch in letMap[digits[ind]]:
                current += ch
                backtrack(ind+1, current)
                current = current[:-1]

        backtrack(0, "")
        return results