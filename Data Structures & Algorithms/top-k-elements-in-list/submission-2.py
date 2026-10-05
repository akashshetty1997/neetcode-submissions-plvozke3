# we can loop each number and when we get a num make a key and add a count we do it for all . then loop the dict by value and return k
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, frequency in my_dict.items():
            bucket[frequency].append(num)

        result = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result
        
