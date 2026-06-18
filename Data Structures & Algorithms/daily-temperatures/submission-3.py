class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        ans = [0]*l
        stack = [] # save index
        for i in range(l):
            # 新數字要進去之前，要先看stack裡面最上面的數字是否較小，如果較小，就要安排ans
            while stack and temperatures[stack[-1]] < temperatures[i]:
                pop_idx = stack.pop()
                ans[pop_idx] = i-pop_idx
            stack.append(i)
        return ans
        