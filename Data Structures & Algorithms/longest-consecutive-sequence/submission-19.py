class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        set_nums = set(nums)
        max_len = 0

        for num in set_nums:
            if num - 1 not in set_nums:   # 只從起點開始
                current = num
                tmp_len = 1

                while current + 1 in set_nums:
                    current += 1
                    tmp_len += 1

                max_len = max(max_len, tmp_len)

        return max_len