class TrieNode:
  def __init__(self, key):
    self.nodes = []
    self.key = key
    self.isEnd = True
  
  def markEnd(self, end):
    self.isEnd = end

class Trie:
  def __init__(self):
    self.root = TrieNode(None)

  def addPattern(self, pattern):
    current = self.root
    for c in pattern:
      if current.nodes is None:
        current.nodes = [TrieNode(key=c)]
        current = current.nodes[0]
      else:
        found = False
        p = None
        for n in current.nodes:
          if n.key == c:
            found = True
            p = n
            break
        
        if not found:
          n = TrieNode(key=c)
          current.nodes.append(n)
          current = n
        else:
          current = p
  
  def makeFrom(self, patterns):
    for pattern in patterns:
      self.addPattern(pattern)


if __name__ == '__main__':
  print('Trie')

  trie = Trie()
  trie.makeFrom('their')
  trie.makeFrom('there')
  trie.makeFrom('answer')
  trie.makeFrom('any')
  trie.makeFrom('bye')
