package main

import (
	"regexp"
	"strings"
)

func isPalindrome(s string) bool {
	reg := regexp.MustCompile("[^a-zA-Z0-9]+")
	s = reg.ReplaceAllString(s, " ")
	s = strings.ToLower(s)

	for i := 0; i < len(s); i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}
