class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        # Since we need to search small idx first, we start travel the nums from front to end.
        # Also, we don't need to compare the repeat combination, thus, 2nd num only start search from i+1 to end.
        for i in range(l):
            for j in range(i+1, l):
                tmp_sum = nums[i]+nums[j]
                if tmp_sum == target:
                    arr = [i, j]
                    return arr
                else:
                    continue
        return False
        