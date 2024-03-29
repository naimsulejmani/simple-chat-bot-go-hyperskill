package main

import (
	// write the missing imports here
	. "fmt"
	. "math"
)

const ToRadians = Pi / 180

func main() {
	// just add the missing prefixes to the functions below.
	var angle float64
	Scanf("%f", &angle)

	angle *= ToRadians // do not modify this line, it converts the angle to radians

	Println(Sin(angle) - Cos(angle))
}
