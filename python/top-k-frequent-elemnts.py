def top_k_frequent(nums, k):
    res = {}
    for n in nums:
        res[n] = res.get(n, 0) + 1

    sorted_map = sorted(res, key=res.get, reverse=True)

    return sorted_map[0:k]
