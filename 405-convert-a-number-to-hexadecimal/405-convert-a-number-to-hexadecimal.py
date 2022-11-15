class Solution:
    def toHex(self, num: int) -> str:
        '''s=""
        if num==-1:
            return "ffffffff"
        if num==0:
            return "0"
        while num>=15:
            s=s+str(num//16)
            num=num%16
        
        if num==10:
            s+='a'
        elif num==11:
            s+='b'
        elif num==12:
            s+='c'
        elif num==13:
            s+='d'
        elif num==14:
            s+='e'
        elif num==15:
            s+='f'
        return s'''
        if num==0:
            return "0"
        m="0123456789abcdef"
        ans=""
        for i in range(8):
            ans=m[num%16]+ans
            num=num//16
        return ans.lstrip('0')