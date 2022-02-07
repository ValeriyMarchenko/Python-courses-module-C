class Node:
    def __init__(self, value = None, next_ = None):
        self.value = value      
        self.next = next_

    def __str__(self):
        return "Node value = " + str(self.value)

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
    
    def clear(self): 
        self.__init__()

    def __str__(self):
        R = ''
        pointer = self.first
        while pointer is not None:
            R += str(pointer.value)
            pointer = pointer.next
            if pointer is not None:
                R += ''
        return R

    def pushleft(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def pushright(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node    
            self.last = new_node

    def popleft(self):
        if self.first is None:
            return None
        
        elif self.first == self.last:
            node = self.first
            self.__init__()
            return node

        else:
            node = self.first
            self.first = self.first.next
            return node

    def popright(self):
        if self.first is None:
            return None

        elif self.first == self.last:
            node = self.first
            self.__init__()
            return node

        else:
            node = self.last
            pointer = self.first
            while pointer.next is not node:
                pointer = pointer.next
            pointer.next = None
            self.last = pointer
            return node

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            node = self.current
            self.current = self.current.next
            return node

    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count

LL = LinkedList()


LL.pushright(1)
LL.pushleft(2)
LL.pushright(3)
LL.popright()
LL.pushleft(4)
LL.pushright(5)
LL.popleft()

print(LL)
print(LL.__len__())