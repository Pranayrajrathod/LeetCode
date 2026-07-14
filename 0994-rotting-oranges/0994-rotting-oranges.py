from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=Queue()
        n=len(grid)
        m=len(grid[0])
        mxans=0
        dir=[[-1,0],[0,-1],[1,0],[0,1]]
        visited=[[0 for i in range (m)] for i in range (n)]
        ans=[[float("inf") for i in range (m)] for i in range (n)]
        gc=0

        for i in range (n):
            for j in range(m):
                if(grid[i][j]==2):
                    q.put([i,j])
                    ans[i][j]=0
                if(grid[i][j]==1):
                    gc+=1
        if(gc==0):
            return 0

        while(q.qsize()>0):
            [i,j]=q.get()
            if(visited[i][j]==1):
                continue
            if(grid[i][j]==1):
                grid[i][j]=2
                gc-=1
            visited[i][j]=1
            if(gc==0):
                break
            for x,y in dir:
                if(i+x<0 or j+y<0 or i+x>=n or j+y>=m or grid[i+x][j+y]==0):
                    continue
                if(visited[i+x][j+y]):
                    continue
                q.put([i+x,j+y])
                ans[i+x][j+y]=min(ans[i+x][j+y],ans[i][j]+1)
                mxans=max(ans[i+x][j+y],mxans)
        
        for i in range (n):
            for j in range (m):
                if(grid[i][j]==1):
                    return -1
        return mxans