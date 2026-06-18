class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        ans = [0]*l
        stack = [] # save index
        for i in range(l):
            if not stack:
                stack.append(i)
                continue
            while stack and temperatures[stack[-1]] < temperatures[i]:
                pop_idx = stack.pop()
                ans[pop_idx] = i-pop_idx
        return ans
        