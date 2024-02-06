class HashMap():
    def __init__(self, size=100):
        #uses linked lists in background not list
        #allocates space on demand, better storage
        self.MAX = 20
        self.storage = [None for i in range(self.MAX)]

    def hashFunction(self, key):
        #applies custom hash function on key, to get a index for the storage list
        sum = 0
        for x in str(key):
            sum += ord(x)
        return sum % self.MAX
    
    def __setitem__(self, key, value):
        index = self.hashFunction(key)
        self.storage[index] = value

    def __getitem__(self, key):
        index = self.hashFunction(key)
        return self.storage[index]
    
    def __delitem__(self, key):
        index = self.hashFunction(key)
        self.storage[index] = None


    def show(self):
        for value in self.storage:
            print(value)

if __name__ == '__main__':
    test = HashMap()
    test['jan 2'] = 100
    test['mar 5'] = 3400
    test['dec 12'] = 'tres'
    print(test['mar 5'])
    test.show()
    print('-------')
    del test['dec 12']
    # print(test.hashFunction('bobby'))
    test.show()