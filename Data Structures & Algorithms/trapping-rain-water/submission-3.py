class Solution:
    def trap(self, height: List[int]) -> int:
        # method: prefix_max, suffix_max
        # water in index i = min(prefix_max, suffix_max) - height[i]
        # total water = sum(array)
        l = len(height)
        prefix_max = [0]*l
        suffix_max = [0]*l
        prefix_max[0] = height[0]
        suffix_max[l-1] = height[l-1]
        water = [0]*l
        for i in range(1, l):
            prefix_max[i] = max(prefix_max[i-1], height[i])
            suffix_max[l-1-i] = max(suffix_max[l-i], height[l-1-i])
        for i in range(1, l-1):
            water[i] = min(prefix_max[i], suffix_max[i]) - height[i]
        print(water)
        return sum(water)

    # def getWaterInInterval(self, height: List[int], left: int, right: int) -> int:
    #     left_height = height[left]
    #     right_height = height[right]
    #     lower = min(left_height, right_height)
    #     water = 0
    #     for i in range(left+1, right):
    #         diff = lower - height[i]
    #         if diff > 0:
    #             water += diff
    #     return water
        