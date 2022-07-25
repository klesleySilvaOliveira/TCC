class DLNode:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class DLinkedList:
   def __init__(self):
      self.begin = None
      self.end = None 
      self.size = 0
	
   def push_front(self, block):
      aux = DLNode(block)
      aux.next = self.begin
      if self.size > 0:
         self.begin.prev = aux
      else:
         self.end = aux
      self.begin = aux
      self.size += 1

   def push_back(self, block):
      aux = DLNode(block)
      aux.prev = self.end
      if self.size > 0:
         self.end.next = aux
      else:
         self.begin = aux
      self.end = aux
      self.size += 1
	
   def list_print(self):
      node = self.begin
      if node is None:
         print("Lista vazia!")
      while (node is not None):
         print(node.data.get_opcode())
         node = node.next

   def pop_front(self):
      aux = self.begin
      if self.size == 1:
         self.size -= 1
         self.begin = None
         self.end = None
      else:
         aux.next.prev = None
         self.size -= 1
         self.begin = self.begin.next
      return aux.data

   def pop_back(self):
      aux = self.end
      if self.size == 1:
         self.size -= 1
         self.begin = None
         self.end = None
      else:
         aux.prev.next = None
         self.size -= 1
         self.end = self.end.prev
      return aux.data

   def get_size(self):
      return self.size