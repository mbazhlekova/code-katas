def search_matrix(matrix, target):
    for r in matrix:
        if r[len(r) - 1] >= target:
            res = binary_search(r, target)
            if res:
                return True

            return False

def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return False

print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 11))


