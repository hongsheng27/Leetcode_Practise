class Node:
  def __init__(self, id = None, count = None):
    self.id = id
    self.count = count
    self.next = None
    self.prev = None
class Recorder:
  # head = Node = tail
  def __init__(self, k):
    self.head = Node()
    self.tail = Node()
    self.head.next = self.tail
    self.tail.prev = self.head
    self.map = {} # id: count
    self.k = k
  def addRecord(self, id, cnt):
    # O(1 + n)
    # if exist in map: add cnt and order
    # if not:
    # add Node to tail of linkedlist
    # add to Map 
    # sort
    if id in self.map:
      node = self.map[id]
      node.count += cnt
      self.sort(node)
    else:
      node = Node(id, cnt)
      self.addToTail(node)
      self.map[id] = node
      self.sort(node)

  def addToTail(self, node):
    before = self.tail.prev

    node.next = self.tail
    node.prev = before

    before.next = node
    self.tail.prev = node
 
  def swap(self, a, b):
    # O(1)
    after = b.next
    before = a.prev

    b.next = a
    a.prev = b

    before.next = b
    b.prev = before
    a.next = after
    after.prev = a

  def sort(self, node):
    # O(n)
    cur = node
    while cur.prev != self.head:
      before = cur.prev
      if (before.count < cur.count or 
      before.count == cur.count and before.id > cur.id):
        self.swap(before, cur)
      else:
        break
  def returnK(self):
    # O(k)
    res = []
    cur = self.head
    for _ in range(self.k):
      cur = cur.next
      res.append(cur.id)
    return res
  
class Solution:
    def topKIDs(self, records, k):
        recorder = Recorder(k)
        for id, cnt in records:
          recorder.addRecord(id, cnt)
        return recorder.returnK()
