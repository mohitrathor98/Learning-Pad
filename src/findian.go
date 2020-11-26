/*
	Write a program which prompts the user to enter a string.
	The program searches through the entered string for the characters ‘i’, ‘a’, and ‘n’. 
*/

package main

import ( 
	"fmt"
	s "strings"
	"bufio"
	"os"
)

func main(){

	var str string
	fmt.Printf("String: ")
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		str = scanner.Text()
	}

	str = s.ToLower(str)
	if(s.HasPrefix(str,"i") && s.HasSuffix(str,"n") && s.Contains(str,"a")){
		fmt.Println("Found!")
	} else {
		fmt.Println("Not Found!")
	}
}