class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_idx = []
        for i, num in enumerate(nums):
            if num == 0:
                zero_idx.append(i)
        if len(zero_idx) > 1:
            return [0 for i in range(len(nums))]
        elif len(zero_idx) == 1:
            idx = zero_idx[0]
            prd = 1
            for i, num in enumerate(nums):
                if i == idx:
                    continue
                else:
                    prd = prd * num
            ans = [0] * len(nums)
            ans[idx] = prd
            return ans
        else:
            prd_max = 1
            ans = []
            for num in nums:
                prd_max = prd_max * num
            for num in nums:
                # ans.append(int(prd_max/num))
                ans.append(prd_max//num)
            return ans


        