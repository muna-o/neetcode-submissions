class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        # sliding window + hashset

        '''
        put the first k elements into a hash set
        '''

        window = set()

        end = min(k + 1, len(nums))

        
        for i in range(end):
            if nums[i] in window:
                return True
            window.add(nums[i])
        for i in range(k + 1, len(nums)):
            window.remove(nums[i - (k + 1)])
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False