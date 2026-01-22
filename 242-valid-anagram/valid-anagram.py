class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if lengths don't match, return False
        if len(s) != len(t):
            return False
        else:
            # create a dict which maps letter -> frequency for s
            counter = dict()
            letters = set()
            for x in s:
                counter[x] = counter.get(x, 0) + 1
                letters.add(x)
            
            # then traverse t and use the same dictionary to check
            for y in t:
                if y in letters:
                    counter[y] -= 1
                else:
                    return False
            
            for _, v in counter.items():
                if v != 0:
                    return False
            
            return True

        