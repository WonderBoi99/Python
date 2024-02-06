class HashMap():
    def __init__(self, size=100):
        #uses linked lists in background not list
        #allocates space on demand, better storage
        self.MAX = 10
        #for collison handling, using chaining solution
        self.storage = [[] for i in range(self.MAX)]

    def hashFunction(self, key):
        #applies custom hash function on key, to get a index for the storage list
        sum = 0
        for x in str(key):
            sum += ord(x)
        return sum % self.MAX
    
    def __setitem__(self, key, value):
        index = self.hashFunction(key)
        found = False
        for i, pair in enumerate(self.storage[index]):
            if len(pair) == 2 and pair[0] == key:
                found = True
                self.storage[index][i] = (key,value)
        if not found:
            self.storage[index].append((key, value))



    def __getitem__(self, key):
        index = self.hashFunction(key)
        for i, pair in enumerate(self.storage[index]):
            if len(pair) == 2 and pair[0] == key:
                return self.storage[index][i]
    
    def __delitem__(self, key):
        index = self.hashFunction(key)
        for i, pair in enumerate(self.storage[index]):
            if len(pair) == 2 and pair[0] == key:
                self.storage[index][i] = None

    def show(self):
        for list in self.storage:
            print(list)

if __name__ == '__main__':
    # test = HashMap()
    # file = open('nyc_weather.csv')
    # heading = True
    # for line in file:
    #     if heading:
    #         heading = False
    #     else:
    #         element = line.strip().split(',')
    #         test[element[0]] = element[1]
    # test.show()
    # print('-----')
    
    # temp = 'Jan'
    # sum = 0
    # for date in range(1,8):
    #     temp += ' {}'.format(date)
    #     sum += int(test[temp][1])
    #     print(temp)
    #     temp = 'Jan'
    # print(sum / 7)

    