class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        
        cnt_s = {}
        cnt_t = {}
        for c in s:
            cnt_s[c] = cnt_s.get(c, 0) + 1
        for c in t:
            cnt_t[c] = cnt_t.get(c, 0) + 1
        print(cnt_s, cnt_s)
        return cnt_s == cnt_t
        