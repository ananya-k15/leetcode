class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # chmap = {}
        # l = len(s)
        # for i in range(0, l, 1) : 
        #     if s[i] not in chmap : 
        #         if t[i] in chmap.values() :
        #             return False
        #         else : 
        #             chmap[s[i]] = t[i]
        #     else : 
        #         if chmap[s[i]] != t[i] : 
        #             return False
        #     print(chmap)
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
        