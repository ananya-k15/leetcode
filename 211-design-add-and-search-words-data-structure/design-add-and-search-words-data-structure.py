class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for let in word:
            if let not in current.children:
                current.children[let] = TrieNode()
            current = current.children[let]
        current.word = True

    def search(self, word: str) -> bool:

        # We use a modified dfs to explore all nodes when we hit a "."

        def dfs(ind, root):
            current = root
            for i in range(ind, len(word)):
                let = word[i]
                if let == ".":
                    for child in current.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if let not in current.children:
                        return False
                    current = current.children[let]
            return current.word
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)