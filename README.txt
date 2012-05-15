This is a simple exercise in Python that helps to highlight some of the basics 
of the language. 

Background:

The Fibonacci Sequence is an infinite series of numbers that begins with 
integers 0 and 1. The  subsequent digit in the sequence is always the sum of the 
last two integers in the series. It looks something like this:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Goal:

Have the program return the nth number within the Fibonacci Sequence, e.g., if 
the user wishes to know the first digit of Fibonacci, the program *must* return 
0. If they wish to know the second digit, the program *must* return 1. If they 
wish to know the 10th digit, the program *must* return 34, so on and so forth. 

Instructions:

1) Run the script 
2) To iteratively compute the value of Fibonacci, use f1(n), where n is the 
desired digit in the sequence.
3) To recursively compute the value of Fibonacci, use f2(n), where n is the 
desired digit in the sequence.
4) To determine whether each program returns the same output for n, run qa(n).

Notes:

1) If you want to see the list being generated iteratively in f1(), just remove 
the '#' from the following line: '#print (i-1), '=', terms'

2) I imagine it is different for each computer, but using recursion, f2(), is 
really only a viable method for determining the first 30 or 40 digits of 
Fibonacci. This is because the number of processes that are being run increase 
exponentially as the value of n increases. If you try f2(100), it will take more 
than a few minutes for the correct value to be returned.

3) For higher digits of Fibonacci, I strongly suggest that you use f1(). It will 
accomplish the task far quicker than f2().