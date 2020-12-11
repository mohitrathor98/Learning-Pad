/*
	Write a program which prompts the user to enter integers and stores the integers in a sorted slice.
	 The program should be written as a loop. Before entering the loop, the program should create an empty
	  integer slice of size (length) 3. During each pass through the loop, the program prompts the 
	  user to enter an integer to be added to the slice. The program adds the integer to the slice, sorts the slice,
	   and prints the contents of the slice in sorted order. The slice must grow in size to accommodate any number
		of integers which the user decides to enter. The program should only quit (exiting the loop) when the user
		 enters the character ‘X’ instead of an integer.
*/

package main

import (
	"fmt"
	"unicode"
	"strconv"
	"sort"
)

func main(){
	num := make([]int, 3)
	i := 2
	for true{
		var x string
		fmt.Scan(&x)
		
		if(x == "x" || x == "X"){
			break
		}
		
		r := []rune(x)
		if(!unicode.IsDigit(r[0])){
			fmt.Println("Integers required, x to exit")
			continue
		}
		
		val,err := strconv.Atoi(x)
		if(err == nil){
			if(i<0){
				num = append(num,val)
			} 
			if (i>=0){
				num[i] = val
				i-=1
			}
			
			sort.Ints(num)
		}
		fmt.Println(num)
	}
}