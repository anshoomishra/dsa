import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        visited = {0: math.inf}
        
        def dfs(total):
            if total <= 0:
                return 0
            
            if total in visited:
                return visited[total]
            

            return visited[total]
        
        return dfs(amount)

if __name__ == "__main__":
    solution = Solution()
    coins = [1,3,4,5]
    amount = 7
    print(solution.coinChange(coins,amount))