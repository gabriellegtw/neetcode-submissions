class PrefixTree:

    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def insert(self, word: str) -> None:
        curr = self
        while word:
            if word[0] not in curr.children:
                curr.children[word[0]] = PrefixTree()
            curr = curr.children[word[0]]
            word = word[1:]

        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.end_of_word
        
    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True
        
        