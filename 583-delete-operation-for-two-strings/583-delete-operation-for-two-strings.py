class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """m=len(word1)
        n=len(word2)
        if m==0:
            return m
        if n==0:
            return n
        if word1[m-1]==word2[n-1]:
            return minDistance(word1[:-1],word2[:-1])
        return 1+min(minDistance(word1[:],word2[:-1]),minDistance(word1[:-1],word2[:]))"""
        
        m=len(word1)
        n=len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                elif word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1])
        return dp[m][n]
            