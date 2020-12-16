"""
Question 18: 
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
it cannot be solved by brute force, and requires a clever method! ;o)
"""

"""
You can assume the triangle is right triangle and its x-coordinate is always increasing 
In this method, A Recursive is used to 'smartly' move to next y-coordinate
Cases that should be considered are first, and last, and in between ones

"""
def calculate_max(list, index=0, counter=0):
    tot_value=0
    if index == 0:
        print(list[index][counter])
        tot_value = list[index][counter] + calculate_max(list, index+1, counter)
        return tot_value
    elif index == len(list):
        print("size of list is {}".format(len(list)))
        return 0
    else:
        
        if list[index][counter] > list[index][counter+1]:
            print(list[index][counter])
            next = list[index][counter] + calculate_max(list,index+1,counter)
            return next
        else:
            print(list[index][counter+1])
            next = list[index][counter+1] + calculate_max(list,index+1,counter+1)
            return next

if __name__ == "__main__":
    nums = list()
    with open('C:/Users/test/Downloads/flasktest/sixth/sixth.txt', 'r') as f:
        for each_line in f:
            temp_list = each_line.split()
            to_int = [int(n) for n in temp_list]
            nums.append(to_int)
    print(calculate_max(nums))

