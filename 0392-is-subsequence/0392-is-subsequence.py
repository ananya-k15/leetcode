class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lt = len(t)
        ls = len(s)
        ind = 0
        sind = 0
        while ((ind < lt) and (sind < ls)) : 
            if s[sind] == t[ind] : 
                sind += 1
                ind += 1
            else : 
                ind += 1    
         
        if sind == ls :
            return True
        else : 
            return False