package main

import "fmt"

func main() {
	// DO NOT delete or modify the code block below!
	var num1, num2, num3 int
	fmt.Scanln(&num1, &num2, &num3)
	intSlice := []int{num1, num2, num3}

	// Write the code to multiply each element of `intSlice` by 2
	// And then print each multiplied element on a new line here or below this comment:
	for _, element := range intSlice {
		fmt.Println(element * 2)
	}
}
