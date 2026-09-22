#Contains Duplicate 
# my approach
# i will loop list of nums and make dict exmaple nums = [1, 2, 3, 3]
# then new_nums = {} where i loops nums each vlaue in nums will be a key , if a value not present in dict i will add and dict value increment by 1 , if it present then i will stop and return false

# Space complexity = O(n) where n is number of items in array nums


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = {}
        for num in nums:
            if num in new_nums:
                return True
            else:
                new_nums[num] = 1
        return False



























# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         new_nums = set()

#         if(len(nums) != 0):
#             for num in nums:
#                 new_nums.add(num)
#         else:
#             return False

#         if(len(new_nums) != len(nums)):
#             return True
#         else:
#             return False
        
        