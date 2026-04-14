class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = []
        max_len = 0
        for c in s:
            if c in sub_str:
                max_len = max(max_len, len(sub_str))
                # pop the "c" in prev_sub_str
                while sub_str and c in sub_str:
                    sub_str = sub_str[1:]
            sub_str += c
        if sub_str:
            max_len = max(max_len, len(sub_str))
        return max_len
        