class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights)
        left = 0
        right = l-1
        max_water = 0
        while left < right:
            width = right - left
            tmp_water = 0
            if heights[left] > heights[right]:
                tmp_water = width * heights[right]
                right -= 1
                max_water = max(max_water, tmp_water)
            else:
                tmp_water = width * heights[left]
                left += 1
                max_water = max(max_water, tmp_water)
        return max_water