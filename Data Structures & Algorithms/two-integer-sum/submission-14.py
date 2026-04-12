class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Sol 2: save a nums_to_idx array, only need to traverse each num once.
        # save time complexity, but waste storage emory
        l = len(nums)
        nums_with_idx = [[nums[i], i] for i in range(l)]
        nums_with_idx = sorted(nums_with_idx)
        i = 0
        j = len(nums_with_idx)-1
        for k in range(l):
            tmp_sum = nums_with_idx[i][0] + nums_with_idx[j][0]
            if tmp_sum == target:
                if nums_with_idx[i][1] > nums_with_idx[j][1]:
                    return [nums_with_idx[j][1], nums_with_idx[i][1]]
                return [nums_with_idx[i][1], nums_with_idx[j][1]]
            elif tmp_sum > target:
                j = j-1
            else:
                i = i+1
        return []



        