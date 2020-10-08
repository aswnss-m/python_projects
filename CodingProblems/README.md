### Daily Coding Challenge

# Find the missing number

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicate and negative numbers as well


>For Example
>	`
>	Input : [3,4,8,-1,1] // Output : 2
>	`
>>	Output is '2' because thats the smallest positive number missing , 2 < 3
>	`
>	Input : [1,2,0] // Output : 3
>	`
>>	Output is '3' because thats the next smallest positive number missing , 3 > 2
>	 

## Algorithm

1.Get the list of integers
2.Find the minimum and maximum value in the list
3.Check whether all the positive integers (i > 0) between minimum and maximum value are present in the list or not
> In the first example '2,5,6,7' is not in the list 
4.Find the smallest among the missing numbers , and print
> In the fisrt case , the smallest is '2'
5.Stop

### Files in this folder

-> _master.py_ //File is ready to run in command line
-> _function.py_ // This contains the algorithm for finding the missing number
-> *master_notebook.ipnyb* //The jupyter notebook for the program
