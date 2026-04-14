class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ans = []
        sorted_nums = sorted(nums)
        for i in range(l-2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            target = 0-sorted_nums[i]
            find = self.twoSum_allpair(sorted_nums, i+1, l-1, target)
            if find:
                for pair in find:
                    get = [sorted_nums[i]]+pair
                    ans.append(get)                
        return ans
            

    def twoSum_allpair(self, numbers: List[int], left: int, right: int, target: int) -> List[List[int]]:
        # Two Pointers technique
        # return all pair version
        # also skip the duplicate comparison
        l = len(numbers)
        i = left
        j = right
        ret = []
        while i<j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                ret.append([numbers[i], numbers[j]])
                i += 1
                j -= 1
                while i<j and numbers[i]==numbers[i-1]:
                    i+=1
                while i<j and numbers[j]==numbers[j+1]:
                    j-=1
        return ret