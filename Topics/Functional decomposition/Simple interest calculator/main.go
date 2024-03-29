package main

import "fmt"

// getData() asks the user to input the `amount` of money, then the `interestRate`
// and last the `numberOfYears` and then returns those three variables
func getData() (float64, float64, float64) {
	var amount, interestRate, numberOfYears float64

	fmt.Scanln(&amount)        // Read the `amount` of money first
	fmt.Scanln(&interestRate)  // Read the `interestRate` second
	fmt.Scanln(&numberOfYears) // Read the `numberOfYears` last

	return amount, interestRate, numberOfYears
}

// calculateSimpleInterest() takes as arguments the `amount`, `interestRate` and `numberOfYears`
// and uses the formula from the problem statement to calculate the `simpleInterest`
// nolint: gomnd // <-- DO NOT delete!
func calculateSimpleInterest(amount, interestRate, numberOfYears float64) float64 {
	simpleInterest := (amount * interestRate * numberOfYears) / 100
	return simpleInterest
}

// printResult() prints the calculated `simpleInterest` and `totalAmount`
// With two decimal places using fmt.Printf() with the `%.2f` format specifier
func printResult(simpleInterest, totalAmount float64) {
	fmt.Printf("The simple interest is %.2f\n", simpleInterest)
	fmt.Printf("The total amount is %.2f\n", totalAmount)
}

// DO NOT delete or modify the contents of the main() function!
func main() {
	amount, interestRate, numberOfYears := getData()
	simpleInterest := calculateSimpleInterest(amount, interestRate, numberOfYears)
	printResult(simpleInterest, amount+simpleInterest)
}
