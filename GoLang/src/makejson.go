/*
	program which prompts the user to first enter a name, and then enter an address. 
	Your program should create a map and add the name and address to the map using the keys “name” and “address”, respectively. 
	Your program should use Marshal() to create a JSON object from the map, and then your program should print the JSON object.
*/

package main

import (
	"fmt"
	"bufio"
	"os"
)

func main(){
	
	//mapv := make(map[string]string)

	var name string
	var address string
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Printf("Name: ")

	if scanner.Scan() {
		name = scanner.Text()
	}

	fmt.Printf("Address: ")
	if scanner.Scan() {
		address = scanner.Text()
	}
}