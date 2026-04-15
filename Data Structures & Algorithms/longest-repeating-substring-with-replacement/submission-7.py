class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count the {"char": freq} in sliding window
        count = {}
        # return max_len
        res = 0
        # left (start) of the sliding windows
        l = 0
        # max freq char in s (not in sliding window)
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res