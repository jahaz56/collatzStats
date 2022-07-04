collatzStats.py

The Collatz algorithm, also known as the 3n + 1 algorithm, consists of the following two operations on a positive integer, n:

    1. If n is even, divide by two.
    2. If n is odd, multiply by three and add one.

These steps are repeated until n becomes 1.  Once n becomes 1, if the above steps are applied, the sequence falls into an 
infinite loop, as 3(1) + 1 = 4, which is divided twice to get back to 1.

The Collatz conjecture states that no matter what seed this algorithm starts with, the sequence will eventually fall into this 
loop.

It certainly seems like this conjecture is true (every number up to 2^40 has been checked) although no one has ever found a 
proof.

This program allows the user to enter a seed and returns three different values relating to its sequence:

    1. The stopping time - This is the number of steps it takes for the value to fall below the seed.
    
    2. The total stopping time - The number of steps to reach 1.

    3. The expansion factor - The maximum value reached divided by the seed.

    Note: In this program, the multiplication step and the subsequent division by 2 are counted as one step since the
    multiplication will always result in an even number.

