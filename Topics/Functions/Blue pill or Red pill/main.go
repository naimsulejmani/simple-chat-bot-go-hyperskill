package main

import "fmt"

// Do not change the code of this function!
func takePill(pill string) string {
	switch pill {
	case "red":
		return "You stay in wonderland, and see how deep the rabbit hole goes."
	case "blue":
		return "The story ends, you wake up in bed and believe what you want to believe."
	default:
		return "You wake up in a strange place, and you don't know what to do."
	}
}

func main() {
	var selection string
	fmt.Scanf("%s", &selection)

	// Call takePill() within fmt.Println() below, and pass 'selection' to takePill() as an argument:
	fmt.Println(takePill(selection))
}
