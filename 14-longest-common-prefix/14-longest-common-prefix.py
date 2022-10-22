class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ''
        m = min(strs)
        M=max(strs)
        i=0
        for i in range(min(len(m),len(M))):
            if m[i] != M[i]: 
                break
        else: 
            i += 1
        return m[:i]