class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # edge case to consider = empty strings!
        # we need to map each string in strs to a key that stores 
        # which letters are in that string + their frequency
        # if we do this for each string, we'll end up mapping 
        # all the anagrams of a string to the same "key"
        # "aet" could be a key for ate, eat and tea.
        # but strings can be 100 letters long, this would mean big keys.
        # alternative: use a fixed length key, like a dictionary that maps
        # letter : freq (there can only be 26 letters!)
        # or a list/tuple of length 26, where freq of a is stored at index 0, 
        # freq of a is stored at index 1, and so on. 

        # create an empty hashmap
        anagrams = dict()

        # loop over all words in strs
        for word in strs:
            # Create a special index for empty strings
            if word == "":
                anagrams[0] = anagrams.get(0, []) + [""]
                continue

            # for each word, initialize a list of length 26 for frequencies
            freq = [0 for x in range(0,26,1)]
        
            # traverse each word, and for each letter
            for letter in word:
                # the index is ascii value of letter - 65 
                # since a is at the 97th position
                # add +1 to the frequencies list
                freq[ord(letter)-97] += 1

            # check if anagrams aleady has this key
            anagram_key = str(freq) # turn to a tuple since dictionary keys must be immutable
            # if so, add this word to the key's value
            # if not, add a new entry to anagrams
            anagram_value = anagrams.get(anagram_key, [])
            anagrams[anagram_key] = anagram_value + [word]

        # extract all the values from anagrams (list of lists)
        return [x[1] for x in anagrams.items()]