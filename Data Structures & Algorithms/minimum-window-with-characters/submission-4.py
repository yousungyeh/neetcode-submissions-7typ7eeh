class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # print(self.isInclude(Counter(s),Counter(t)))
        # return ""
        # if len(s) < len(t):
        #     return ""
        # if len(s) == len(t):
        #     return s if s == t else ""
        ans = ""
        l = len(s)
        r = 0
        l = 0
        cnt_tmp_str = Counter()
        cnt_t = Counter(t)
        for c in s:
            l += 1
            cnt_tmp_str[c] += 1
            while self.isInclude(cnt_tmp_str, cnt_t):
                # update min_length(ans)
                tmp_ans = s[r:l]
                print("update ans:", tmp_ans)
                if len(tmp_ans) < len(ans) or not ans:
                    ans = tmp_ans
                cnt_tmp_str[s[r]] -= 1
                r += 1
        return ans

    def isInclude(self, cnt_s: Counter, cnt_t: Counter) -> bool:
        for key, val in cnt_t.items():
            if key not in cnt_s:
                return False
            elif cnt_s[key] < cnt_t[key]:
                return False
            else:
                continue
        return True
        