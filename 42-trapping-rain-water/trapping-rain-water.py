class Solution:
    def trap(self, height: List[int]) -> int:
        prevmax = [0]*len(height)
        postmax = [0]*len(height)
        result = 0
        for i in range(1,len(height)):
            prevmax[i] = max(prevmax[i-1],height[i-1])
        for i in range(len(height)-2,-1,-1):
            postmax[i] = max(postmax[i+1],height[i+1])
        for i in range(len(height)):
            res = min(prevmax[i],postmax[i])-height[i]
            if res>0:
                result+=res
        return result


