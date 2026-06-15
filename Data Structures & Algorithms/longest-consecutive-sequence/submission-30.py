class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        current_num = sorted_nums[0]
        max_conse_cnt = 1
        current_cnt = 1
        for num in sorted_nums[1:]:
            if num == current_num:
                continue
            elif num == current_num+1:
                # update current_num
                current_cnt += 1
                current_num = num
                # update max_cnt
                max_conse_cnt = max(max_conse_cnt, current_cnt)
            else:
                # update current_num
                current_cnt = 1
                current_num = num
        return max_conse_cnt
        