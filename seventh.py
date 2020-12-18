"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

"""
Using Memoization method, Solved Question by brute force.
If python support big-enough numbers, it takes O(n) time
The point is that The question is solvable by smart mathematical ways using binet's formular 
but its more likely to practice programming skill, so it seems using dynamic programming is better one 
"""
def fib(digit):
    # F2 = 1, F1 = 1
    result = 1
    previous = 1
    index = 2
    while len(str(result)) < digit:
        result += previous
        previous = result - previous
        index += 1
    print(index)

if __name__ == "__main__":
    fib(1000)
