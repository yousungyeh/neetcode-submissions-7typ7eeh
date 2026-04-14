class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(nums)
        max_len = 1
        prev = sorted_nums[0]
        tmp_len = 1
        for num in sorted_nums[1:]:
            if num == prev:
                continue
            if num == prev+1:
                tmp_len += 1
                max_len = max(max_len, tmp_len)
            else:
                tmp_len = 1
            prev = num
        return max_len