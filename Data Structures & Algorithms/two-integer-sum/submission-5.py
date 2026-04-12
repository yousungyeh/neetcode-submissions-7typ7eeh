class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        # Since we need to search small idx first, we start traverse the nums from front to end.
        for i in range(l):
            for j in range(i+1, l):
                # Also, we don't need to compare the repeat combination, thus, 2nd num only start search from i+1 to end.
                tmp_sum = nums[i]+nums[j]
                if tmp_sum == target:
                    # Follow the output spec patterns, we return an array (list)
                    arr = [i, j]
                    return arr
                else:
                    continue
        return False
        