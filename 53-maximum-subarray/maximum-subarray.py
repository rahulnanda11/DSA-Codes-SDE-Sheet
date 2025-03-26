class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub=nums[0]
        cur_sub=nums[0]
        for n in nums[1:]:
            cur_sub=max(cur_sub+n,n)
            max_sub=max(cur_sub,max_sub)
        return max_sub