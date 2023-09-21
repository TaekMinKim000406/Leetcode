class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # 오른쪽에서부터 탐색하며 오름차순이 끝나는 지점 찾기
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # i가 음수인 경우, 입력 리스트가 가장 큰 순열임
        if i == -1:
            nums.reverse()  # 입력 리스트를 뒤집어서 가장 작은 순열로 만듭니다.
            return

        # i 이후에서 nums[i]보다 큰 첫 번째 수를 찾기(없으면 j=i-1이 됨)
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1

        # nums[i]와 nums[j]를 스왑
        nums[i], nums[j] = nums[j], nums[i]

        # i 이후 부분을 오름차순으로 정렬하여 다음 순열 완성
        nums[i + 1:] = reversed(nums[i + 1:])

        

