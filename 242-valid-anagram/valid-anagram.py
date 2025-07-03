class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        letters = dict()

        for ch in s:
            letters[ch] = letters.get(ch, 0) + 1
        
        for ch in t:
            if ch in letters.keys():
                if letters[ch] == 1:
                    del letters[ch]
                else:
                    letters[ch] -= 1
            else:
                return False
        
        if len(letters) == 0:
            return True
        return False