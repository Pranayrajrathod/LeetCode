from queue import Queue
class Solution:
    def findCircleNum(self, al: List[List[int]]) -> int:
        q=Queue()
        n=len(al)
        ans=0
        visited=[0 for i in range (n)]
        am=[[] for i in range (n)]
        for i in range (n):
            for j in range(n):
                if(al[i][j]==1 and i!=j):
                    am[i].append(j)
        print(am)
        for i in range (n):
            if(visited[i]==0):
                q.put(i)
                ans+=1
                while(q.qsize()>0):
                    k=q.get()
                    if(visited[k]==1):
                        continue
                    visited[k]=1
                    for each in am[k]:
                        q.put(each)
        return ans