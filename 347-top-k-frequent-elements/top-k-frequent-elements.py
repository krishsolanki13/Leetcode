class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        freq = [[] for _ in range(len(nums)+1)]
        for num,count in count.items():
            freq[count].append(num)
        res=[]
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res