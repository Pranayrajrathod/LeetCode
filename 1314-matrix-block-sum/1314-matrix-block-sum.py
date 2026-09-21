class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m=len(mat)
        n=len(mat[0])
        ps=[[0 for i in range (n+1)] for i in range (m+1)]
        
        for i in range (1,m+1):
            for j in range (1,n+1):
                ps[i][j]=ps[i-1][j]+ps[i][j-1]-ps[i-1][j-1]+mat[i-1][j-1]
        
        ans=[[0 for i in range(n)] for j in range (m)]
        print(ps)
        for i in range (m):
            for j in range (n):
                r1=max(0,i-k) 
                c1=max(0,j-k) 
                r2=min(m,i+k+1) 
                c2=min(n,j+k+1)
                print(i,j,ps[max(0,i-k)][max(0,j-k)])
                ans[i][j]=ps[r2][c2]-ps[r1][c2]-ps[r2][c1]+ps[r1][c1]
        return ans