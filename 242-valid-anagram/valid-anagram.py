class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if lengths don't match, return False
        if len(s) != len(t):
            return False
        else:
            # create a dict which maps letter -> frequency for s
            s_dict = dict()
            for x in s:
                s_dict[x] = s_dict.get(x, 0) + 1
            
            # then traverse t and use the same dictionary to check
            for y in t:
                if y in s_dict.keys():
                    s_dict[y] -= 1
                else:
                    return False
            
            for _, v in s_dict.items():
                if v != 0:
                    return False
            
            return True

        