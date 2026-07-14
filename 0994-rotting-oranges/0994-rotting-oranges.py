from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=Queue()
        n=len(grid)
        m=len(grid[0])
        mxans=0
        dir=[[-1,0],[0,-1],[1,0],[0,1]]
        # visited=[[0 for i in range (m)] for i in range (n)]
        ans=[[float("inf") for i in range (m)] for i in range (n)]
        gc=0

        for i in range (n):
            for j in range(m):
                if(grid[i][j]==2):
                    q.put([i,j,0])
                    ans[i][j]=0
                if(grid[i][j]==1):
                    gc+=1
        if(gc==0):
            return 0
        while(q.qsize()>0):
            [i,j,time]=q.get()
            grid[i][j]=2
            for x,y in dir:
                if(i+x<0 or j+y<0 or i+x>=n or j+y>=m or grid[i+x][j+y]==0):
                    continue
                if(grid[i+x][j+y]==1):    
                    q.put([i+x,j+y,time+1])
                    mxans=max(time+1,mxans)
                    grid[i+x][j+y]=2
                    gc-=1
        if(gc!=0):
            return -1
        return mxans