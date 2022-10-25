class UnionFind:
    def __init__(self,size) -> None:
        self.root = [i for i in range(size)]
    
    def find(self,x):
        return self.root[x]
        

    def union(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            print(x_root,y_root)
            for i in range(len(self.root)):
                if self.root[i] == y_root:
                    self.root[i] = x_root

    def is_connected(self,x,y):
        return self.find(x) == self.find(y)
    
if __name__== "__main__":
    uf = UnionFind(5)
    uf.union(3,4)
    uf.union(1,5)
    print(uf.is_connected(1,3))


if __name__ == "__main__":
    pass
