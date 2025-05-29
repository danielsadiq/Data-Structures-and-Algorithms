class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head= None
  
  def insert_at_beginning(self, data):
    node = Node(data, self.head)
    self.head = node

  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data)
      return
    itr = self.head
    while itr.next:
      itr = itr.next
    itr.next = Node(data)

  def insert_values(self, data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data)
  
  def print(self):
    if self.head is None:
      print("Linked list is empty")
      return
    itr = self.head
    llstr = ""
    while itr:
      llstr += str(itr.data) + "--> "
      itr = itr.next
    print(llstr)

  def get_length(self):
    count = 0
    itr = self.head
    while itr:
      count += 1
      itr = itr.next
    return count
  
  def my_remove_at(self, index):
    itr = self.head
    prev = None
    count = 0
    if index == 0:
      self.head = self.head.next
      return

    while count < index-1:
      count+=1
      itr = itr.next
      prev = itr
    while count < index + 1:
      count +=1
      itr = itr.next
      prev.next = itr
    
    print(prev.data)

  def remove_at(self, index):
    if index < 0 or index >=self.get_length():
      raise Exception("Invalid Index")
    if index == 0:
      self.head = self.head.next
      return
    count = 0
    itr = self.head
    while itr:
      if count == index-1:
        itr.next = itr.next.next
        break
      itr = itr.next
      count +=1

  def insert_at(self, data, index):
    if index <=0 or index >self.get_length():
      raise Exception("Invalid Index")
    
    if index == 0:
      self.insert_at_beginning(data)

    count = 0
    itr = self.head
    while itr:
      if count == index-1:
        itr.next = Node(data, itr.next)
        break
      itr = itr.next
      count +=1

      

ll = LinkedList()

ll.insert_at_beginning(5)
ll.insert_at_beginning(89)
ll.insert_at_end(78)
ll.insert_at_beginning(47)
ll.insert_at_end(102)
ll.insert_at_end(32)

# ll.insert_values([23,79,45,68,87])
ll.print()
# ll.remove_at(2)
ll.insert_at(50,4)

ll.print()