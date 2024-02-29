class Solution:
    def search(nums, target):
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        if nums[start] <= nums[mid]:
            if target > nums[mid] or target < nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if target < nums[mid] or target > nums[end]:
                end = mid - 1
            else:
                start = mid + 1
    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 4))
