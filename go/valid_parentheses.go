package main

import "github.com/golang-collections/collections/stack"

func isValid(s string) bool {
	stack := stack.New()

	for _, char := range s {
		if char == '(' {
			stack.Push(')')
		} else if char == '[' {
			stack.Push(']')
		} else if char == '{' {
			stack.Push('}')
		} else if char != stack.Pop() {
			break
		}
	}
	return stack.Len() == 0
}
