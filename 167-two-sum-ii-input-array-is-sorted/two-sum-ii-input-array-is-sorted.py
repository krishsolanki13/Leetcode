class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l<r:
            diff = target-numbers[l]
            while r>l and numbers[r]>diff:
                r-=1
            if numbers[r]==diff:
                return [l+1,r+1]
            else:
                l+=1
                r=len(numbers)-1
        return [-1,-1]