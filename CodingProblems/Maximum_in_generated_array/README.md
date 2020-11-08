### Daily Coding Problems

# Get Maximum in Generated Array

You are given an integer n. An array nums of length n + 1 is generated in the following way:

* nums[0] = 0
* nums[1] = 1
* nums[2 * i] = nums[i] when 2 <= 2 * i <= n
* nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

Return the maximum integer in the array nums​​​.

> For Example
>>Input: n = 7
>> Output: 3
>> Explanation: According to the given rules:
>> nums[0] = 0
>> nums[1] = 1
>> nums[(1 * 2) = 2] = nums[1] = 1
>> nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
>> nums[(2 * 2) = 4] = nums[2] = 1
>> nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
>> nums[(3 * 2) = 6] = nums[3] = 2
>> nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
>>Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.
>
>

## Algorithm

1. Start

2. Get the value of n // the limit

3. Generate an zero array of size = n + 1 // all the elements are : [ 0, 0, 0, 0]

4. Set the second element of the array, ie: array[1] = 1

5. For i in the range of length of the array change the value of the elements according the conditions given.

6. Find the maximum of the array generated.
