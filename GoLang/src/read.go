/*
	program should prompt the user for the name of the text file.
	Your program will successively read each line of the text file and
	create a struct which contains the first and last names found in the file. Each struct
	created will be added to a slice, and after all lines have been read from the file, your
	program will have a slice containing one struct for each line in the file. After reading all lines from the file,
	your program should iterate through your slice of structs and print the first and last names found in each struct.
*/

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var filename string
	fmt.Printf("File Name: ")
	fmt.Scan(&filename)

	type Name struct {
		firstName string
		lastName  string
	}

	const (
		maxLength = 20
	)

	f, err := os.Open(filename)
	if err == nil {
		fileData := make([]byte, 500)
		_, e := f.Read(fileData)
		if e == nil {
			data := string(fileData)
			d := strings.Split(data, "\n")
			var slice []Name
			for _, v := range d {
				k := strings.Split(v, " ")

				var p Name

				if len(k[0]) > maxLength {
					p.firstName = k[0][:maxLength]
				} else {
					p.firstName = k[0]
				}

				if len(k[1]) > maxLength {
					p.lastName = k[1][:maxLength]
				} else {
					p.lastName = k[1]
				}

				slice = append(slice, p)
			}

			for _, v := range slice {
				fmt.Println("First Name: " + v.firstName + "\tLast Name: " + v.lastName)
			}

		} else {
			fmt.Println("Can't read data")
		}
	} else {
		fmt.Println("File NOT found")
	}
}
