class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[0 for i in range (m)] for i in range (n)]
        dp[0][0]=grid[0][0]
        for i in range (1,m):
            dp[0][i]=grid[0][i]+dp[0][i-1]
        # print(dp)
        for i in range (1,n):
            for j in range (m):
                if(j==0):
                    dp[i][j]=dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j])+grid[i][j]
        return dp[n-1][m-1]