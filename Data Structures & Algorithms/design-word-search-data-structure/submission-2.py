class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        # Instantiate an empty string 
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                # Store in a dictionary with the key as a letter
                # The Node as a value is like a placeholder
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.isEnd = True
                
    def search(self, word: str) -> bool:
        def dfs(curr, index):
            if curr is None:
                return False

            if index >= len(word):
                if curr.isEnd:
                    return True
                else:
                    return False

            char = word[index]

            if char == '.':
                # All the values are the TrieNodes
                for child in curr.children.values():
                    if dfs(child, index + 1):
                        return True
                        # Else, go to next child
                return False

            if char in curr.children:
                return dfs(curr.children[char], index + 1)

            return False

        return dfs(self.root, 0)

        
