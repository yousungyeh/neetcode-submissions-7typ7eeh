class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        save the char that is the most freq until s[:right].
        bc it is the most possible char that we need to maintain.
        """
        # count the {"char": freq} in sliding window
        count = {}
        # return max_len
        res = 0
        # left (start) of the sliding windows
        l = 0
        # max freq char in s[:right] (means until now) (not in sliding window)
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            
            # sliding window that we need to maintain target char(max freq char until s[:right])
            while (r - l + 1) - maxf > k:
                # move sliding window
                count[s[l]] -= 1
                l += 1
            # update max_len
            res = max(res, r - l + 1)

        return res