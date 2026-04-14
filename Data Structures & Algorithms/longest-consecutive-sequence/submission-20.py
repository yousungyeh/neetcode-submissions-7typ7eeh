class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        set_nums = set(nums)
        max_len = 0

        for num in set_nums:
            # identify it is start_num or not
            if num - 1 not in set_nums:
                current = num # start_num
                tmp_len = 1

                # start start_num to traverse nums to find its consective seq.
                while current + 1 in set_nums:
                    current += 1
                    tmp_len += 1

                max_len = max(max_len, tmp_len)

        return max_len