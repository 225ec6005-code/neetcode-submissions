class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]*len(nums)
        prefix=1
        for i in range(1,len(nums)):
            pre[i]= prefix*nums[i-1]
            prefix=pre[i]
        post=[1]*len(nums)
        postfix=1

        for i in range(len(nums)-2,-1,-1):
            post[i]=postfix* nums[i+1]
            postfix=post[i]

        res=[pre[i] * post[i] for i in range(len(nums))] 
        return res  