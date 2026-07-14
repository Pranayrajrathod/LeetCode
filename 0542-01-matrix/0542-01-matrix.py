from queue import Queue
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=Queue()
        n=len(mat)
        m=len(mat[0])
        visited=[[0 for i in range (m)] for i in range (n)]
        ans=[[float("inf") for i in range(m)] for j in range(n)]
        dir=[[0,1],[1,0],[-1,0],[0,-1]]

        for i in range(n):
            for j in range(m):
                if(mat[i][j]==0):
                    q.put([i,j])
                    ans[i][j]=0
        while(q.qsize()>0):
            [i,j]=q.get()
            visited[i][j]=1
            for x,y in dir:
                ni, nj = i + x, j + y
                if 0 <= ni < n and 0 <= nj < m:
                    if ans[ni][nj] > ans[i][j] + 1:
                        ans[ni][nj] = ans[i][j] + 1
                        q.put([ni, nj])     
        return ans