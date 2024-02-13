'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
TEST CASE 1

	Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

TEST CASE 2

	Input: nums = [3,2,4], target = 6
Output: [1,2]


TEST CASE 3

	Input: nums = [3,3], target = 6
Output: [0,1]


'''

# nums = list(input("list: ").split(","))
# target = int(input("target: "))
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if int(nums[i]) + int(nums[j]) == target:
#             print(i,j)

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
