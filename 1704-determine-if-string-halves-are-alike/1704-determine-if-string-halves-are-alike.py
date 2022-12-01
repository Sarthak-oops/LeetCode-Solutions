class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c1=0
        c2=0
        v={'a','e','i','o','u','A','E','I','O','U'}
        for x in range(len(s)):
            if x>=(len(s)//2) and s[x] in v:
                c2+=1
            elif s[x] in v:
                c1+=1
        if c1==c2:
            return True
        return False