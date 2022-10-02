class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=len(word1)
        m=len(word2)
        s=""
        if n<m:
            for i in range(n):
                s=s+word1[i]+word2[i]
            s=s+word2[n:]
        elif n>m:
            for i in range(m):
                s=s+word1[i]+word2[i]
            s=s+word1[m:]
        else:
            for i in range(n):
                s=s+word1[i]+word2[i]
        return s