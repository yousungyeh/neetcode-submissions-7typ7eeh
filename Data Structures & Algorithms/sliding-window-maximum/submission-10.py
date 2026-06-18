class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # 存 index
        ans = []

        for i, num in enumerate(nums):
            # 1. 移除已經滑出 window 的 index
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # 2. 維持 deque 對應的值是遞減的
            while dq and nums[dq[-1]] < num:
                dq.pop()

            # 3. 把目前 index 加進 deque
            dq.append(i)

            # 4. 當第一個完整 window 形成後，開始記錄答案
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans