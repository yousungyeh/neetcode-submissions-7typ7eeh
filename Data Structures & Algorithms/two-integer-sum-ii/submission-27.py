class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two Pointers technique
        # Best, but only handle this case, if there're lots of correct pair, it failed
        l = len(numbers)
        i = 0
        j = l - 1
        while i<j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return[i+1, j+1]

                    
        