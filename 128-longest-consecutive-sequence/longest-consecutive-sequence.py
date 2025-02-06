class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0
        length = 0
        for num in num_set:
            if (num-1) not in num_set:
                length = 1
                while (num+length) in num_set:
                    length += 1
                result = max(length,result)
        return result