class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = Counter(s1)
        l=0
        r = l+len(s1)-1
        while r<len(s2):
            b = Counter(s2[l:r+1])
            if b==a:
                return True
            l+=1
            r+=1
        return False




            