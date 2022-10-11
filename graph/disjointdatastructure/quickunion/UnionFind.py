class UnionFind:
    def __init__(self,size):
        i = 0
        self.root = []
        while i < size:
            self.root.append(i)
            i+=1
    
    def find(self,x):
        if self.root[x] == x:
            return x
        return self.find(self.root[x])
        
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.root[rooty] = rootx
            
    def connected(self,x,y):
        return self.find(x) == self.find(y)
    
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
print(uf.connected(3, 9))  # true
print(uf.connected(1, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
uf.union(1,9)
print(uf.connected(1, 9))  # true
print(uf.connected(4, 9))  # true
print(uf.root)