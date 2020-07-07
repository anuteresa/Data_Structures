class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, new_data):
        newnode = Node(new_data)
        if (self.head == None):
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

    def display(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


#REVERSE OF LINKED LIST
    def Reverse(self):
      prev = None
      current = self.head
      while (current != None):
        next = current.next
        current.next = prev
        prev = current
        current = next
      self.head = prev

slist=Linkedlist()
slist.push(1)
slist.push(2)
slist.push(8)
slist.push(9)
slist.push(4)
slist.push(5)
slist.push(4)

slist.display()
slist.Reverse()
slist.display()