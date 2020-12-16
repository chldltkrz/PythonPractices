"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

# Dict of individual unique numbers, note that 1000 is a special last case only appear once, so
# dont have to be included in the dect
nums = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
    30: "Thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
    100: "hundred",
}


# The method is converting incoming integer into string.


def translate(number: int) -> str:
    translation = ""
    # Should count Special cases that a number is divisible by 10 or 100, 
    # cases 1-99
    if number > 0 and number < 100:
        if number % 10 == 0 or number < 20:
            translation = nums[number]
        else:
            translation = nums[number - (number % 10)] + nums[number % 10]

    # cases 100-999 - added "and" expression
    elif number >= 100 and number < 1000:
        if number % 100 == 0:
            translation = nums[(number - (number % 100))/100] + nums[100]
        else:
            translation = nums[(number - (number % 100))/100] + \
                nums[100] + "and" + translate(number % 100)

    # cases 1000
    elif number == 1000:
        translation = "onethousand"

    ''.join(x.strip() for x in translation)
    return translation


def evaluate(target: int) -> int:
    count = 0
    for _ in range(1, target):
        count += len(translate(_))
    return count


if __name__ == "__main__":
    print(evaluate(1001))
