class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = len(s)
        max_len = 0
        for i in range(l):
            start_char = s[i]
            tmp_len = 1
            remain_replace_times = k
            for j in range(i+1, l):
                if s[j] == start_char:
                    tmp_len += 1
                elif remain_replace_times > 0:
                    remain_replace_times -= 1
                    tmp_len += 1
                else:
                    break
            tmp_len = min(remain_replace_times+tmp_len, l)
            max_len = max(max_len, tmp_len)
        return max_len
        