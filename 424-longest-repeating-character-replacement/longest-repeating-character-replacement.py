class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chardict = {}
        res = 0 
        l=r=0
        while r<len(s):
            chardict[s[r]] = 1 + chardict.get(s[r],0)
            while (r-l+1)-max(chardict.values())>k:
                chardict[s[l]] -= 1
                l+=1
            res = max(res,r-l+1)
            r+=1
        return res