"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

#cases 1-19
#cases 20-99
#cases 100
#cases 101-999 - added and expression
#cases 1000 

def translate(number:int) -> str:
    traslation = ""
    
    
    return traslation;
    

def evaluate(target:int) -> int:
    count = 0
    for _ in range(target):
        count += translate(_)
    return count
    
if __name__ == "__main__":
    print(evaluate(1000))
    