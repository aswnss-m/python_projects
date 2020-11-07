### Daily Coding Challenge

# Run-length Encoding

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to 
represent repeated successive charactors as a single count and charactor.

> For Example
>
>
>> `Input : "AAAABBBCCDAA"`
>>
>> `Output : "4A3B2C1D2A"`
>
>> `Input : "AABBCC"`
>>
>> `Output : "2A2B2C"`
>
>

## Algorithm

1. Get the string

2. Set the first charactor as a key , at pos = 0 and count = 1 // initial position and count

3. Starting from next position , compare the charactor to the key . If they are same : Increase the count by 1. 

4. Continue step 3 until a different charactor is found , then set the new charactor as key , and set count = 1 // reseting the count 

5. Put all these details together as a string , and output

6. Stop