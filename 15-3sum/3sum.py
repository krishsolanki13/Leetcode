class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        res = []
        for i in range(len(nums)-1):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                l=i+1
                r=len(nums)-1
                while l<r:
                    sum = nums[i] + nums[l] + nums[r]
                    if sum>0:
                        r-=1
                    elif sum<0:
                        l+=1
                    else:
                        res.append([nums[i],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while r>l and nums[r]==nums[r-1]:
                            r-=1
                        l+=1
                        r-=1                
        return res  
                 
