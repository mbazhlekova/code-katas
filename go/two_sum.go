package two_sum

func twoSum(nums []int, target int) []int {
	seenNums := map[int]int{}
	for i, num := range nums {
		potentialMatch := target - num
		if j, ok := seenNums[potentialMatch]; ok {
			return []int{i, j}
		}
		seenNums[num] = i
	}
	return []int{}
}
