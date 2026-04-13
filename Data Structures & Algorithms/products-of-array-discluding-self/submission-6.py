class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Sol 3:
        prefix product + suffix product
        
        """
        l = len(nums)
        prefix = [0] * l
        prefix[0] = nums[0]
        suffix = [0] * l
        suffix[-1] = nums[-1]
        for i in range(1, l):
            prefix[i] = prefix[i-1]*nums[i]
            j = l-i-1
            suffix[j] = suffix[j+1]*nums[j]
        return [suffix[1]] + [prefix[i-1]*suffix[i+1] for i in range(1,l-1) ] + [prefix[l-2]]
        