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