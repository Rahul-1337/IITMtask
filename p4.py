'''
Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 
Test case 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Test case 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

'''


# so if we devide the haystack in equal parts as needle and then we can search,
# for ex, needle length is 3, devide haystack in equal parts of 3, then you caan find index
# how do we devide it in equal length


# different approach, match the first letter from the needle to haystack 
def find_needle(haystack, needle):
    haystack = input("haystack is: ")
    needle  = input("needle is: ")
    output = haystack.find(needle)
    return output