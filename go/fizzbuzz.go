package main

import "fmt"

func fizzbuzz(n int) {
	for _, num := range n {
		if num % 15 == 0 {
			fmt.Println("FizzBuzz")
		} else if num % 3 == 0 {
			fmt.Println("Fizz")
		} else if num % 5 == 0 {
			fmt.Println("Buzz")
		} else {
			fmt.Println(num)
		}
	}
}

func main() {
	fizzbuzz(100)
}
