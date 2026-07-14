class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n=len(grid)
        m=len(grid[0])

        def dfs(grid,i,j):
            if(i<0 or i>=n or j<0 or j>=m or grid[i][j]=="0"):
                return
            dir=[[1,0],[0,1],[-1,0],[0,-1]]
            grid[i][j]="0"
            for x,y in dir:
                dfs(grid,i+x,y+j)
        ans=0
        for i in range(n):
            for j in range (m):
                if(grid[i][j]=="1"):
                    ans+=1
                    dfs(grid,i,j)
        return ans