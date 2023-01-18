import collections
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        seen = collections.defaultdict(int)
        answer = []
        for num in nums:
            seen[num] += 1
        
        while k > 0:
            max_value = 0
            for key, value in seen.items():
                if value > max_value:
                    max_value = value
                    max_key = key
            seen.pop(max_key)
            answer.append(max_key)
            k -= 1
        return answer
