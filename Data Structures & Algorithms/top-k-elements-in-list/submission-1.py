# Approach:
'''
    Created a frequency dict by looping nums and counting each element.
    Created a bucket of size len(nums) + 1 where each index represents a frequency.
    For each key-value in the dict, append the key into buckets[frequency].
    Iterate buckets in reverse (highest frequency first), collect items until we have k results.

    Time complexity  - O(n) — multiple loops but all linear, no nested n*n work.
    Space complexity - O(n) — dict + buckets both scale with input size.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_nums = defaultdict(int)
        for num in nums:
            new_nums[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in new_nums.items():
            buckets[value].append(key)
        
        result = []

        for bucket in buckets[::-1]:
            for item in bucket:
                result.append(item)   
                if len(result) == k:
                    return result

        return result