class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for element in nums:
            if count == 0:
                candidate = element

            if element == candidate:
                count += 1
            else:
                count -= 1

        return candidate
        