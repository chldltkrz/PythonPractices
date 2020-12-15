
"""
Euler project 16
This problem is about get value of sum of each digits of 2 ** 1000
Note that math library does no good here because it uses its scientific expression
just use 2**1000 expression to calculate the sum as a whole
"""
sum = 0

for n in str(2**1000):
    sum += int(n)
    
print(sum)


