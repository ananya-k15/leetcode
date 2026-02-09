class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a dictionary to store 
        # anagram_info : list of words
        # anagram_info = tuple with letters in word in asc order + their frequencies
        anagrams = dict()

        # for each word in strs
        for word in strs:
            if len(word) == 0:
                anagrams[""] = anagrams.get("", []) + [""]
                continue

            # compute anagram info into a sorted tuple
            letters = dict()
            for l in word:
                letters[l] = letters.get(l, 0) + 1
            key = tuple(sorted(letters.items()))

            # check if it already exists in dict
            # if yes, update list value to include this word
            # if no, add entry with this word
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]

        # loop through dict to create a list of lists
        # or return all the values of the anagrams dict
        return list(anagrams.values())
