# Problem 1 - Value Swap (2pts)
# Swap the values 18 and 38 in the list below
import random
my_list = [27, 32, 18,  2, 11, 57, 14, 38, 19, 91]

value = my_list[2]
my_list[2] = my_list[7]
my_list[7] = value

print(my_list)
print()


# Problem 2 - Selection Sort (8 pts)
# Make a selection sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.
sort_me = [655, 722, 736, 314, 59, 778, 632, 477, 230, 556, 353, 769, 622, 731, 683, 233, 524, 186, 694, 507, 443, 833, 270, 373, 567, 775, 34]

def select_sort(my_list):
    for currentpos in range(len(my_list)):
        smallpos = currentpos
        for scanpos in range(currentpos + 1, len(my_list)):
            if my_list[scanpos] < my_list[smallpos]:
                smallpos = scanpos
        value = my_list[smallpos]
        my_list[smallpos] = my_list[currentpos]
        my_list[currentpos] = value
        return my_list

def print_list(my_list):
    for item in my_list:
        print("{:3}".format(item), end=" ")
    print()

print_list(sort_me)
select_sort(sort_me)
print_list(sort_me)
'''
def sort(my_list):
    for pos in range(1, len(my_list)): # pos is the first thing in my_list
        key_pos = pos
        scan_pos = key_pos - 1
        key_val = my_list[key_pos]
        while scan_pos >= 0 and my_list[scan_pos] > key_val: # makes sure key value is still less than the value we are scanning
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1 # moves the scan position to the left
        my_list[scan_pos + 1] = key_val
        return my_list

sort(sort_me)

def sort(my_list):
    for curent_pos in range(len(my_list)):
        # Find the position that has the smallest number
        # Start with the current position
        smallest_pos = curent_pos
        # Scan left to right (end of the list)
        for scan_pos in range(curent_pos + 1, len(my_list)):
            # Is this position smallest?
            if my_list[scan_pos] < my_list[smallest_pos]:
                # It is, mark this position as the smallest
                min_pos = scan_pos
        # Swap the two values
        temp = my_list[smallest_pos]
        my_list[smallest_pos] = my_list[curent_pos]
        my_list[curent_pos] = temp

def print_list(my_list):
    for item in my_list:
        print("{:3}".format(item), end=" ")
    print()

print_list(sort_me)
sort(sort_me)


#def sort(list):
    #key = 0
    #while key <= len(list):
        #if list[key] > list[key + 1]:
'''

# Problem 3 - Insertion Sort (8 pts)
# Make an insertion sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.
sort_me2 = [551, 138, 802, 954, 569, 372, 454, 366, 936, 959, 958, 202, 474, 658, 108, 424, 523, 611, 557, 0, 733, 903, 788, 850, 11, 12, 975]

# Problem 4 - Efficiency? (10 pts)
# Modify your two functions so that they track the number of times
# you iterate through the big loop, and the inner loop of the sort.
# Make the functions print each value.  Run the sorts on the list below.

sort_me3 = [77, 29, 59, 69, 86, 40, 47, 40, 74, 44, 58, 78, 9, 8, 13, 99, 3, 57, 19, 48, 55, 50, 94, 69, 98, 30, 37, 29, 40, 29, 36, 32, 26, 85, 61, 51, 70, 96, 90, 89, 91, 88, 68, 4, 4, 74, 15, 72, 5, 91, 76, 6, 56, 80, 72, 87, 63, 86, 48, 24, 17, 23, 30, 41, 7, 64, 16, 19, 40, 63, 14, 95, 44, 58, 1, 6, 45, 55, 52, 54, 44, 36, 50, 6, 96, 66, 8, 46, 48, 48, 75, 25, 39, 30, 70, 44, 38, 90, 49, 70]
