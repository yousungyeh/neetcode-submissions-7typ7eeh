class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        "Brute Force Method (Inline)"
        """
        Space: O(1)
        Time: O(n*k)
        """
        return [max(nums[i:i+k]) for i in range(len(nums)-k+1)]
        