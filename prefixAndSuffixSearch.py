class TrieNode:
    def __init__(self):
        self.children = {}
        self.weight = -1

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()

        for weight, word in enumerate(words):
            for i in range(len(word) + 1):
                pattern = word[i:] + '{' + word
                current = self.root

                for c in pattern:
                    if c not in current.children:
                        current.children[c] = TrieNode()
                    current = current.children[c]
                    current.weight = weight

    def f(self, pref: str, suff: str) -> int:
        pattern = suff + '{' + pref
        curr = self.root

        for c in pattern:
            if c not in curr.children:
                return -1
            curr = curr.children[c]

        return curr.weight

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)