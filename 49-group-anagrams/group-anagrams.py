class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for str in strs:
            count = [0]*26
            for c in str:
                count[ord(c)-ord('a')]+=1
            ans[tuple(count)].append(str)
        return list(ans.values())