class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        next_pointer = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[next_pointer] = nums[i]
                print(i)
                next_pointer += 1

        return next_pointer 

        