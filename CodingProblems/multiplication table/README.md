## Daily Coding Problem

# Multiplication Table
Suppose you have a multiplication table that is N by N. 
That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).
Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.
>
For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:
```
 | 1 | 2 | 3 | 4 | 5 | 6 |

 | 2 | 4 | 6 | 8 | 10 | 12 |

 | 3 | 6 | 9 | 12 | 15 | 18 |

 | 4 | 8 | 12 | 16 | 20 | 24 |

 | 5 | 10 | 15 | 20 | 25 | 30 |

 | 6 | 12 | 18 | 24 | 30 | 36 |
```
>
And there are 4 12's in the table.

## Algorithm
1. Start
2. Get the value of N and X.
3. Create a nested loop that created the element in a NxN matrix.
4. Check the value againt X ,
5. If the match increase the count , else continue
6. At the end of the loop return the count.
7. Stop