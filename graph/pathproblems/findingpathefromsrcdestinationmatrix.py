visited = {}
def find_path(m,n,grid):
    if m > len(grid) or n > len(grid[0]):
        return 0
    if (m,n) in visited:
        return visited[(m,n)]
    if m == len(grid)-1  and n == len(grid[0])-1:
        return 1

    visited[(m,n)] = find_path(m+1,n,grid)+find_path(m,n+1,grid)
    return visited[(m,n)]

if __name__ == "__main__":
    grid = [
        [1,0,0,1],
        [1,1,0,1],
        [1,1,0,1],
        [1,0,0,1],
    ]
   
    print(find_path(0,0,grid))