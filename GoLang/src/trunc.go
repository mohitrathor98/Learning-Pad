package main

import "fmt"

func main(){
	var f float64
	fmt.Printf("Floating point number: ")
	fmt.Scan(&f)

	fmt.Printf("Truncated int format %0.0f\n",f)
}
