class Solution:          
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for i in range(0, len(strs), 1) : 
            alpha = ''.join(sorted(strs[i]))
            anagrams[alpha] = [strs[i]] + anagrams.get(alpha, [])
        return anagrams.values()
        