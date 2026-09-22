
#Two Sum

# as i know there be always one valid answer  nums = [3,4,5,6], target = 7
#   i will loop nums and take first eelemnt exmaple 3 - target and wahtever comes i chekc if its persent if not then move too next which is 4

# space complxity O(n) where n is number of elments in nums array
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], idx]

            seen[num] = idx
        