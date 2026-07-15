class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        l=len(nums)
        if(s&1):
            return 1==2
        ss=s//2

        dp=[[False for i in range (s+1)] for i in range (l)]
        for i,each in enumerate(nums):
            dp[i][each]=True
        dp[0][nums[0]]=True
        dp[0][0]=True
        for i in range (1,l): 
            for j in range (s):
                if(dp[i-1][j-nums[i]]==True or dp[i-1][j]==True):
                    dp[i][j]=True
        return dp[l-1][ss]==True