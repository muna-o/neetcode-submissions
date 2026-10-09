class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency_map = {}

        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 1
            else:
                frequency_map[num] += 1 

        max_element = 0
        max_frequency = 0

        for num, frequency in frequency_map.items():
            if frequency > max_frequency:
                max_frequency = frequency
                max_element = num

        return max_element

        