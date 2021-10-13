package duplicates

func containsDuplicates(nums []int) bool {
	seen := make(map[int]int)
	for _, num := range nums {
		if _, ok := seen[num]; ok {
			return true
		} else {
			seen[num] = 1
		}
	}
	return false
}
