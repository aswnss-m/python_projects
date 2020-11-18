### Daily Coding Problems

# Find the Unique Number

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicate integer.

> For Example
>> ` Input : [ 6, 1, 3, 3, 3, 6, 6 ] `
>> ` Ouput : 1 `
>
>> `Input : [ 13, 19, 13, 13] `
>> `Output : 19`
>
>

## Algorithm

1. Start

2. Get the Array

3. Starting from the first position, check the element is present in the rest of the array , ie: excluding the element

4. If True , then move to next element and repeat 3

5. Else return the element

6. Stop

