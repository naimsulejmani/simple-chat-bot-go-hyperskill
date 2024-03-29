package main

import "fmt"

func main() {
	var year int
	fmt.Scanln(&year)

	if year%4 == 0 && year%100 != 0 || year%400 == 0 {
		fmt.Println("Leap year")
	} else {
		fmt.Println("Regular year")
	}
}
