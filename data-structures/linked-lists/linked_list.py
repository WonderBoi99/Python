class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def add_to_head(self, data):
        node = Node(data, self.head)
        self.head = node

    def __str__(self):
        temp = ''
        if self.head == None:
            temp = "Linked List is empty"
        else:
            itr = self.head
            while itr:
                temp += "Data: {} \n".format(itr.data)
                itr = itr.next
        return temp
        

ll = LinkedList()
ll.add_to_head(100)
print(ll)
