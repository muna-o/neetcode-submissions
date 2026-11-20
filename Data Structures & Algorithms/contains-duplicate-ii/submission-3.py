class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k <= 0:
            return False

        window = set()

        for i, val in enumerate(nums):
            if val in window:
                return True

            window.add(val)

            if len(window) > k:
                window.remove(nums[i - k])

        return False
        