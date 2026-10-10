class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m - 1
        second = n - 1

        for i in range(len(nums1) - 1, -1, -1):
            if first >= 0 and second >= 0:
                nums1[i] = max(nums1[first], nums2[second])

                if nums1[first] >= nums2[second]:
                    first -= 1
                else:
                    second -= 1
            elif first < 0:
                nums1[i] = nums2[second]
                second -= 1
            else: 
                nums1[i] = nums1[first]
                first -= 1

