class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        ans = []
        for i in range(l-k+1):
            ans.append(max(nums[i:i+k]))
        return ans
        