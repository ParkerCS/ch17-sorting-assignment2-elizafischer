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



def select_sort(sort_me):
    countouter = 0
    countinner = 0
    for currentpos in range(len(sort_me)):
        countouter += 1
        smallpos = currentpos
        for scanpos in range(currentpos + 1, len(sort_me)):
            countinner += 1
            if sort_me[scanpos] < sort_me[smallpos]:
                smallpos = scanpos
        value = sort_me[smallpos]
        sort_me[smallpos] = sort_me[currentpos]
        sort_me[currentpos] = value
    print("Outer Count:" , countouter, "Inner Count:" , countinner)
    return sort_me

# Organizes and prints the items in the list
def print_list(my_list):
    for item in my_list:
        print("{:3}".format(item), end=" ")
    print()

print("Selection Sort")
print_list(sort_me)
select_sort(sort_me)
print_list(sort_me)


# Problem 3 - Insertion Sort (8 pts)
# Make an insertion sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.
sort_me2 = [551, 138, 802, 954, 569, 372, 454, 366, 936, 959, 958, 202, 474, 658, 108, 424, 523, 611, 557, 0, 733, 903, 788, 850, 11, 12, 975]
'''
def insertion_sort(my_list):
    for pos in range(1, len(my_list)):
        key_pos = pos
        scan_pos = key_pos - 1
        key_val = my_list[key_pos]
        while scan_pos >= 0 and my_list[scan_pos] > key_val:
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1
        my_list[scan_pos + 1] = key_val
        return my_list
'''
def insertion_sort(my_list):
    go = 0
    countouter = 0
    countinner = 0
    for i in range(len(my_list)):
        countouter += 1
        go +=1
        for pos in range(1 + go, len(my_list)):
            countinner += 1
            key_pos = pos
            scan_pos = key_pos - 1
            key_val = my_list[key_pos]
            while scan_pos >= 0 and my_list[scan_pos] > key_val:
                my_list[scan_pos + 1] = my_list[scan_pos]
                scan_pos -= 1
            my_list[scan_pos + 1] = key_val
    print("Outer Count:", countouter, "Inner Count:", countinner)
    return my_list

print("\nInsertion Sort")
print_list(sort_me2)
insertion_sort(sort_me2)
print_list(sort_me2)


# Problem 4 - Efficiency? (10 pts)
# Modify your two functions so that they track the number of times
# you iterate through the big loop, and the inner loop of the sort.
# Make the functions print each value.  Run the sorts on the list below.
sort_me3 = [77, 29, 59, 69, 86, 40, 47, 40, 74, 44, 58, 78, 9, 8, 13, 99, 3, 57, 19, 48, 55, 50, 94, 69, 98, 30, 37, 29, 40, 29, 36, 32, 26, 85, 61, 51, 70, 96, 90, 89, 91, 88, 68, 4, 4, 74, 15, 72, 5, 91, 76, 6, 56, 80, 72, 87, 63, 86, 48, 24, 17, 23, 30, 41, 7, 64, 16, 19, 40, 63, 14, 95, 44, 58, 1, 6, 45, 55, 52, 54, 44, 36, 50, 6, 96, 66, 8, 46, 48, 48, 75, 25, 39, 30, 70, 44, 38, 90, 49, 70]

print("\nEfficiency")
print_list(sort_me3)
insertion_sort(sort_me3)
print_list(sort_me3)

