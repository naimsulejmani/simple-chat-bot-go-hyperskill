package main

import "fmt"

func main() {
	var number int
	fmt.Scanf("%d", &number)

	// Write your code here.
	switch {
	case number > 0:
		fmt.Println("Positive!")
	case number < 0:
		fmt.Println("Negative!")
	default:
		fmt.Println("Zero!")

	}
}
