class Solution:
    def reverseWords(self, s: str) -> str:
        res=" ".join(s.split()[::-1])
        return res