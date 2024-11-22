#
# @lc app=leetcode.cn id=208 lang=python
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

    # // Inserts a word into the trie.
    # public void insert(String word) {
    #     TrieNode node = root;
    #     for (int i = 0; i < word.length(); i++) {
    #         char currentChar = word.charAt(i);
    #         if (!node.containsKey(currentChar)) {
    #             node.put(currentChar, new TrieNode());
    #         }
    #         node = node.get(currentChar);
    #     }
    #     node.setEnd();
    # }

    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.lookup = {}

    # def insert(self, word: str) -> None:
    #     """
    #     Inserts a word into the trie.
    #     """
    #     tree = self.lookup
    #     for a in word:
    #         if a not in tree:
    #             tree[a] = {}
    #         tree = tree[a]
    #     # 单词结束标志
    #     tree["#"] = "#"
        

    # def search(self, word: str) -> bool:
    #     """
    #     Returns if the word is in the trie.
    #     """
    #     tree = self.lookup
    #     for a in word:
    #         if a not in tree:
    #             return False
    #         tree = tree[a]
    #     if "#" in tree:
    #         return True
    #     return False
        

    # def startsWith(self, prefix: str) -> bool:
    #     """
    #     Returns if there is any word in the trie that starts with the given prefix.
    #     """
    #     tree = self.lookup
    #     for a in prefix:
    #         if a not in tree:
    #             return False
    #         tree = tree[a]
    #     return True


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/5_tree/tries
"""