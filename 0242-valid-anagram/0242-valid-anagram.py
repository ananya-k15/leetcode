class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        track = dict()
        for i in s :
            if track.get(i) != None :
                track[i] += 1
            else : 
                track[i] = 1
        for k,v in track.items() :
            if v != t.count(k) :
                return False
        return True