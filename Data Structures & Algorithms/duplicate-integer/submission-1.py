class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = set()

        if(len(nums) != 0):
            for num in nums:
                new_nums.add(num)
        else:
            return False

        if(len(new_nums) != len(nums)):
            return True
        else:
            return False
        
        