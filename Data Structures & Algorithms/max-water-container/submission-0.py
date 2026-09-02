class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        maxarea = 0
        while l < r :
            l_bar = heights[l]
            r_bar = heights[r]
            maxarea=max(maxarea , min(l_bar,r_bar)*(r-l))
            if l_bar<=r_bar :
                l+=1
            else :
                r-=1
        return maxarea
