package main

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	hash := make(map[rune]int)
	for _, char := range s {
		hash[char]++
	}

	for _, char := range t {
		hash[char]--
	}

	for _, value := range hash {
		if value != 0 {
			return false
		}
	}
	return true
}
