class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        numWords = [len(i.split(" ")) for i in sentences]
        return max(numWords)