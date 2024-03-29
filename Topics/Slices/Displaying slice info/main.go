package main

import "fmt"

func main() {
	// DO NOT delete or modify the code block below:
	var length, capacity int
	fmt.Scanln(&length, &capacity)
	numbers := make([]int, length, capacity)

	// Write the code below to print the `numbers` slice len(), cap(), and its elements:
	fmt.Printf("len=%d cap=%d elements=%v", length, capacity, numbers)
}
