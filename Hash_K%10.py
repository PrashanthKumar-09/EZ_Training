# Method 1

class Node:
    def __init__(self, k, val):
        self.key = k
        self.val = val
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, k, val):
        index = k % self.size
        if self.table[index] is None:
            self.table[index] = Node(k, val)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = Node(k, val)

    def display(self):
        for i in range(self.size):
            current = self.table[i]
            print(f'{i}:', end=" ")
            while current is not None:
                print(f'{current.key}', end=" -> ")
                current = current.next
            print("None")
keys = [10,16,62,100,20,86,72,7,76,99]
hash_table = HashTable(10)

for key in keys:
    hash_table.insert(key, key)

hash_table.display()

print("-"*110)

# Method 2

class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
class Hashtable:
    def __init__(self):
        self.size=10
        self.table=[None]*self.size
    def insert(self, data):
        index=data%10
        if self.table[index] is None:
            self.table[index]=Node(index)
        curr=self.table[index]
        while curr.next is not None:
            curr=curr.next
        curr.next=Node(data)
    def display(self):
        for i in range(self.size):
            curr=self.table[i]
            while curr is not None:
                print(curr.value,"->",end=" ")
                curr=curr.next
            print(None)
data=[10,16,62,100,20,86,72,7,76,99]
hs=Hashtable()
for i in data:
    hs.insert(i)
hs.display()