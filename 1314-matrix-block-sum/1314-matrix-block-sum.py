class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m=len(mat)
        n=len(mat[0])
        ans=[[0 for i in range (n)] for i in range (m)]

        for i in range (m):
            for j in range (n):
                cs=0
                for p in range (i-k,i+k+1):
                    if(p<0 or p>=m):
                        continue
                    for q in range (j-k,j+k+1):
                        if(q<0 or q>=n):
                            continue
                        cs+=mat[p][q]
                ans[i][j]=cs
        return ans