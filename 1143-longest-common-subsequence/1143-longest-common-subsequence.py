class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        """dp=[[-1]*(n+1)]*(m+1)
        
        def check(s1,s2,m,n,dp):
            if m==0 or n==0:
                dp[m][n]=0
                return dp[m][n]
            if dp[m][n]!=-1:
                return dp[m][n]
            
            if s1[m-1]==s2[n-1]:
                dp[m][n]=1+check(s1,s2,m-1,n-1,dp)
                return dp[m][n]
            dp[m][n]= max(check(s1,s2,m,n-1,dp),check(s1,s2,m-1,n,dp))
            return dp[m][n]
        dp=[[0]*(n+1)]*(m+1)
        return check(text1,text2,m,n,dp)
        """
        def check(s1,s2):
            m=len(s1)
            n=len(s2)
            dp = [[0] * (n+1) for _ in range(m+1)]
            for i in range(1,m+1):
                for j in range(1,n+1):
                    
                    if s1[i-1]==s2[j-1]:
                        dp[i][j]=1+dp[i-1][j-1]
                    else:
                        dp[i][j]=max(dp[i][j-1],dp[i-1][j])
            return dp[m][n]
        return check(text1,text2)