# Sorting Algorithms

This folder contains various sorting algorithms used in programming for sorting and arranging data.
Understanding and learning to implement these algo's is an important skill to have for a programmer.

All these sorting algorithm are written in such a way that they are east to 
grasp and understand for a beginner level programmer

## Files

<details>
<summary>1.<a href="https://github.com/aswnss-m/python_projects/blob/master/Sorting/insertion_sort.py">Insertion Sorting</a>
<br>
<b>Insertion Sort</b> is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.</summary>
<br>The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
Algorithm

To sort an array of size n in ascending order:
<ol>
  <ul> Iterate from arr[1] to arr[n] over the array. </ul>
  <ul> Compare the current element (key) to its predecessor.</ul>
<ul> If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.</ul>
  </ol><br>

<img src="https://upload.wikimedia.org/wikipedia/commons/4/42/Insertion_sort.gif">

</details>

<details>
<summary>2.<a href="https://github.com/aswnss-m/python_projects/blob/master/Sorting/selection_sort.py">Selection Sorting</a>
<br>
<b>Selection Sort</b> is noted for its simplicity and has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited.</summary> <br>
The algorithm divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front (left) of the list and a sublist of the remaining unsorted items that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.
  
Algorithm
<blockquote>
arr[] = 64 25 12 22 11

// Find the minimum element in arr[0...4]
// and place it at beginning
11 25 12 22 64

// Find the minimum element in arr[1...4]
// and place it at beginning of arr[1...4]
11 12 25 22 64

// Find the minimum element in arr[2...4]
// and place it at beginning of arr[2...4]
11 12 22 25 64

// Find the minimum element in arr[3...4]
// and place it at beginning of arr[3...4]
11 12 22 25 64 
</blockquote>
<br>
<img src= "https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif" style="transform:rotate(-90deg)">
</details>
<details>
	<summary>
		3. <a href="https://github.com/aswnss-m/python_projects/blob/master/Sorting/bubble_sort.py">Bubble Sort</a>
		<br><b>Bubble Sort</b> is a simple sorting algorithm. This sorting algorithm is comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order.
	</summary> <br>
	Bubble sort should be avoided in the case of large collections. It will not be efficient in the case of a reverse-ordered collection. 

	<blockquote>

	Step-by-step example

Take an array of numbers " 5 1 4 2 8", and sort the array from lowest number to greatest number using bubble sort. In each step, elements written in bold are being compared. Three passes will be required;

First Pass 	
    ( 5 1 4 2 8 ) → ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
    ( 1 5 4 2 8 ) → ( 1 4 5 2 8 ), Swap since 5 > 4
    ( 1 4 5 2 8 ) → ( 1 4 2 5 8 ), Swap since 5 > 2
    ( 1 4 2 5 8 ) → ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
Second Pass
    ( 1 4 2 5 8 ) → ( 1 4 2 5 8 )
    ( 1 4 2 5 8 ) → ( 1 2 4 5 8 ), Swap since 4 > 2
    ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
    ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )

Now, the array is already sorted, but the algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

Third Pass
    ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
    ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
    ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
    ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
	</blockquote>
	<img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif">
</details>