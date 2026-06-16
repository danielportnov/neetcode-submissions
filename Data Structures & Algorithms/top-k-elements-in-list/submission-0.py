class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        for i in range(k):
            top_key = max(freq, key=freq.get)
            freq.pop(top_key)
            res.append(top_key)

        return res