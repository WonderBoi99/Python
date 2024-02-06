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

    def add_to_tail(self, data):
        if self.head == None:
            self.add_to_head(data)
            return
        else:
            itr = self.head
            node = Node(data, None)
            #finding last element
            while itr.next:
                itr = itr.next
            itr.next = node

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Index is out of bounds")
        elif index == 0:
            self.add_to_head(data)
        else:
            count = 0
            itr = self.head
            while itr.next:
                if count == index-1:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1
            
    
    def get_length(self):
        count = 0 
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def __str__(self):
        temp = ''
        if self.head == None:
            temp = "Linked List is empty"
        else:
            itr = self.head
            while itr:
                temp += "{} => ".format(itr.data)
                itr = itr.next
        return temp
    
        

ll = LinkedList()
ll.add_to_head(200)
ll.add_to_head(100)
ll.add_to_tail(300)
ll.insert_at(3, 5000)
print(ll)
print(ll.get_length())
