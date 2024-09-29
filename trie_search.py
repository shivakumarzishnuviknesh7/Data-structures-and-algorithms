class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        result = []
        self._collect_all_words(node, prefix, result)
        return result

    def _collect_all_words(self, node, prefix, result):
        if node.is_word:
            result.append(prefix)
        for char, child_node in node.children.items():
            self._collect_all_words(child_node, prefix + char, result)


# Example  usage:
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("application")
trie.insert("banana")
trie.insert("bat")

# Autocomplete suggestions for 'app'
suggestions = trie.starts_with("app")
print(suggestions)

# Output: ['app', 'apple', 'application']





