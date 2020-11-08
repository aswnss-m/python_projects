### Dailt Coding Problems

# Edit Distance

The edit distance between two strings refers to the minimum number of character insertions, substituitions and deletions required to change one string to the other. 

> For Example
> 
>
>> `Input : initial  = "kitten" `
>> `        final = "sitting"`
>>  `Output : 3`
>
> Output is 3 because 
> subtitute the "k" for "s"
> subtitute the "e" for "i"
> and append "g"
>
>

## Algorithm

1. Start

2. Get both initial and final words

3. Check the lengths of both words and choose the minimum length

4. The difference of the lengths will give the no.of deletions to be done , add it to the distance

5. Keeping the smaller length as a reference check equality of charactors at respective positions of the final word to the initial word , if they are different add the no.of difference to the distance

6. Return the final distance 

7. Stop