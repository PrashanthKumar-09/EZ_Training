
class Hash:
    def __init__(self,size):
        self.size=size
        self.table=[0]*self.size
    def insert(self,data):
        index=data%self.size
        if self.table[index]==0:
            self.table[index]=data
        else:
            self.index=self.search(index)
            if self.index is not None:
                self.table[self.index]=data
    def search(self,start_index):
        ori=start_index
        index=(start_index+1)%self.size
        while index!=ori:
            if self.table[index]==0:
                return index
            index=(index+1)%self.size
        print("hash table full")
        return None
m=[47,22,16,15,20,7,39,56,62,100,98,94,41]
x=Hash(13)
for i in m:
    x.insert(i)
print(x.table)