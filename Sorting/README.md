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

1: Iterate from arr[1] to arr[n] over the array.
2: Compare the current element (key) to its predecessor.
3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

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
