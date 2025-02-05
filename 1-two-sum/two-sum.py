class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        encountered = {}
        for i,n in enumerate(nums):
            difference = target - n
            if difference in encountered:
                return [encountered[difference],i]
            else:
                encountered[n] = i
        return [-1,-1] 