from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c=Counter(nums)
        mx=max(c)
        # print(mx)
        dp=[0 for i in range (mx+1)]
        dp[0]=c[0]
        dp[1]=max(c[0],c[1])
        for i in range (2,mx+1):
            dp[i]=max((c[i]*i)+dp[i-2],dp[i-1])
        # print(dp)
        return dp[mx]