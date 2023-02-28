class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def mincost(grid):
            m=len(grid)
            n=len(grid[0])
            dp=[[0]*n for i in range(m)]
            for i in range(m):
                for j in range(n):
                    if i==0 and j==0:
                        dp[i][j]=grid[0][0]
                    else:
                        if i>0:
                            topval=grid[i][j]+dp[i-1][j]
                        else:
                            topval=grid[i][j]+float('inf')
                        if j>0:
                            leftval=grid[i][j]+dp[i][j-1]
                        else:
                            leftval=grid[i][j]+float('inf')
                        dp[i][j]=min(topval,leftval)
            return dp[-1][-1]
        return mincost(grid)