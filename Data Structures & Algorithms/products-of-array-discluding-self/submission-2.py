class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = 1
        post = 1
        n = len(nums)
        output = [1]*n
        for i in range(n):
            output[i] = pre
            pre *= nums[i]
        for j in range(n):
            k  = -j-1
            output[k] *= post
            post *= nums[k]
        return output 



