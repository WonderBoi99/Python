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

    def get_size(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def __str__(self):
        result = 'start => '
        if self.head == None:
            return 'LinkedList is empty'
        else:
            itr = self.head
            while itr:
                result += f'{itr.data} => '
                itr = itr.next
            result += 'end'
            return result
        
    def insert_at_start(self, value):
        node = Node(value, self.head)
        self.head = node
    
    def insert_at_end(self, value):
        if self.head == None:
            self.insert_at_start(value)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node = Node(value, None)

    def insert_values(self, values):
        for val in values:
            self.insert_at_end(val)
    
    def insert_at(self, index, data):
        if index >= self.get_size():
            raise Exception(f'{index} is out of range')
        elif index == 0:
            self.insert_at_start(data)
            return
        else:
            count = 0 
            itr = self.head
            while itr:
                if count == index-1:
                    node = Node(data, itr.next)
                    itr.next = node
                    return
                else:
                    count += 1
                    itr = itr.next
        
    def insert_after(self, data_after, data):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data, itr.next)
                itr.next = node
                return
            else:
                itr = itr.next
        raise Exception(f'{data_after} not in ll')
    
    def remove_val(self, value):
        if self.get_size() == 0:
            raise Exception('ll is empty')
        if self.head.data == value:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                return
            else:
                itr = itr.next
        raise Exception(f'{value} not in ll')

ll = LinkedList()
# print(ll)
# print(f'Size of LL = {ll.get_size()}')

# print('inserted three elements at the start')
# ll.insert_at_start(3)
# ll.insert_at_start(2)
# ll.insert_at_start(1)
# print(ll)
# print(f'Size of LL = {ll.get_size()}')

# print('inserted three elements at the end')
# ll.insert_at_end(1)
# ll.insert_at_end(2)
# ll.insert_at_end(3)
# print(ll)
# print(f'Size of LL = {ll.get_size()}')

# print('inserted a list to ll')
# ll.insert_values([1,2,3,4,5,6,7,8,9,10])
# print(ll)
# print(f'Size of LL = {ll.get_size()}')

# print('inserted a index')
# ll.insert_values([1,2,3,4,5,6,7,8,9,10])
# print(ll)
# print(f'Size of LL = {ll.get_size()}')
# ll.insert_at(9,11)
# print(ll)
# print(f'Size of LL = {ll.get_size()}')

# print('inserted a after value')
# ll.insert_values([1,2,3,4,5,6,7,8,9,10])
# print(ll)
# print(f'Size of LL = {ll.get_size()}')
# ll.insert_after(10,2000)
# print(ll)
# print(f'Size of LL = {ll.get_size()}')

# ll.remove_val(500)
# print(ll)
# print(f'Size of LL = {ll.get_size()}')

