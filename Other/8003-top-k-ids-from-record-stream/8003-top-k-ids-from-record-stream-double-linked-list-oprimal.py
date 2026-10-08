
class Node:
  def __init__(self, id = None, count = None):
    self.id = id
    self.count = count
    self.next = None
    self.prev = None
    self.inTopK = False
class Recorder:
  def __init__(self, k):
    self.head = Node()
    self.tail = Node()
    self.head.next = self.tail
    self.tail.prev = self.head
    self.map = {} # {id: Node}
    self.k = k
    self.length = 0

  def addRecord(self, count, id):
    if id in self.map:
      node = self.map[id]
      node.count += count
      if node.inTopK:
        self.sort(node)
      else:
        kth = self.tail.prev
        if self.higher(node, kth):
          self.replaceTail(node)
          kth.inTopK = False
          node.inTopK = True
          self.sort(node)
    else:
      node = Node(id, count)
      self.map[id] = node

      if self.length < self.k:
        self.addToTail(node)
        node.inTopK = True
        self.length += 1
        self.sort(node)
      else:
        kth = self.tail.prev
        if self.higher(node, kth):
          self.replaceTail(node)
          kth.inTopK = False
          node.inTopK = True
          self.sort(node)

  def higher(self, a, b):
    if a.count != b.count:
      return a.count > b.count
      
    return a.id < b.id


  def replaceTail(self, node):
    replaced = self.tail.prev
    before = replaced.prev
    
    node.next = self.tail
    node.prev = before

    before.next = node
    self.tail.prev = node
    
    
  def addToTail(self, node):
    before = self.tail.prev
    
    node.next = self.tail
    node.prev = before

    before.next = node
    self.tail.prev = node
    
  def swap(self, a, b):
    before = a.prev
    after = b.next

    b.next = a
    a.prev = b

    before.next = b
    b.prev = before
    after.prev = a
    a.next = after

  def sort(self, node):
    cur = node
    while cur.prev != self.head:
      before = cur.prev
      if not self.higher(before, cur):
        self.swap(before, cur)
      else:
        break

  def returnK(self):
    res = []
    cur = self.head.next
    while cur != self.tail:
      res.append(cur.id)
      cur = cur.next
    return res
  
class Solution:
    def topKIDs(self, records, k):
        recorder = Recorder(k)
        for id, cnt in records:
          recorder.addRecord(cnt, id)
        return recorder.returnK()