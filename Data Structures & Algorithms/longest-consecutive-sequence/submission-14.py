class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        max_len = 1
        prev = sorted_nums[0]
        tmp_len = 1
        for num in sorted_nums[1:]:
            if num == prev:
                continue
            if num == prev+1:
                prev = num
                tmp_len += 1
                if max_len < tmp_len: # update max_len
                    max_len = tmp_len
            else:
                prev = num
                tmp_len = 1
        return max_len