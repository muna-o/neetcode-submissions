class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        # sliding window + hashset

        '''
        put the first k elements into a hash set
        '''

        window = set()

        for i in range(len(nums)):
            if i > k:
                window.remove(nums[i - k - 1])
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False