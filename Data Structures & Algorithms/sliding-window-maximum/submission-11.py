class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # 存 index
        ans = []

        for i, num in enumerate(nums):
            # 1. 移除已經滑出 window 的 index
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # 2. 維持 deque 對應的值是遞減的，因為新的數值進來時，只要曾經比較小的數值，都不需要留在dq。
            while dq and nums[dq[-1]] < num:
                dq.pop()

            # 3. 把目前 index 加進 deque(進去之前的判斷在步驟2，很重要，需要先把較小的數字全部丟出去)
            dq.append(i)

            # 4. 當第一個完整 window 形成後，開始記錄答案，也就是還在track前幾個nums時不需要append即可。
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans