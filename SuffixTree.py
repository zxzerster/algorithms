class Trie:
  # Trie Node
  class Node:
    def __init__(self):
      self.nodes = [None for x in range(0, 26)]
      self.isEnd = False
    
    def char(self):
      for i in range(0, 26):
        if self.nodes[i] is not None:
          return chr(i + ord('a'))
    
      return None

  def __init__(self):
    self.root = Trie.Node()
  
  def _addPattern(self, pattern):
    if pattern is None or len(pattern) < 1: return

    current = self.root
    for c in pattern:
      index = ord(c) - ord('a')
      if not current.nodes[index]:
        current.nodes[index] = Trie.Node()
      current = current.nodes[index]

    current.isEnd = True

  def makeFrom(self, patterns):
    if patterns is None or len(patterns) < 1: return
    for p in patterns:
      self._addPattern(p)

if __name__ == '__main__':
  print('Trie')

  trie = Trie()
  trie.makeFrom(["hello", "Hi"])