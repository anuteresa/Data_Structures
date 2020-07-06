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
# COUNT THE NODES IN THE LINKED LIST
    def count(self):
        count = 0
        temp = self.head
        while (temp != None):
            count += 1
            temp = temp.next
        return count


slist = Linkedlist()
slist.push(3)
slist.push(2)
slist.push(4)
slist.push(7)
slist.push(9)
slist.display()
print("Count of nodes present in the list: " + str(slist.count()));