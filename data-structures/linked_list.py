'''
To understand benefits of Linked Lists, I need to should learn how dynamic arrays work in python

Array
When you first create an array, it will allocate a specific amount of memory (lets say 5)
Already this isnt most memory efficient as our array is empty
Then say are performing an insert a index 0, it will shift every element forward by 1, time consuming
if you array is full, it will allocate double the initial memory and copy over, again speed issue and memory inefficent
continous memory

linked list
random memory
insert is easier, add new data in random location and get address, give it to previous element
memory is used when needed

the advantage array has over linked list is indexing (O(i) for array, cant index for ll has to search so O(n))
'''









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

    def insert_values(self, values):
        for value in values:
            self.add_to_tail(value)

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head.data == data_after:
            node = Node(data_to_insert, self.head.next)
            self.head.next = node
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data_after:
                node = Node(data_to_insert, itr.next.next)
                itr.next.next = node
                return
            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next
            
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
ll.insert_at(1, 5000)
ll.insert_values(["banana","mango","grapes","orange"])
print(ll)
ll.remove_by_value("banana")
print(ll)
ll.insert_after_value("mango","apple")
print(ll)
ll.insert_after_value(100,"apple")
print(ll)

#test