class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
  
        for i in range(len(nums1)-m):
            nums1.remove(0)
        nums = nums1[:m]
        nums2 = nums2[:n]
        nums1.extend(nums2)
        nums1.sort()
        

