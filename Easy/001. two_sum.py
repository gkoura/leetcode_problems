class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        helper_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            # Check if complement exists in the dictionary
            if complement in helper_dict:
                return [helper_dict[complement], i]
            else:
                helper_dict[num] = i



def main():
    nums = [2, 7, 11, 15]
    target = 9
    solution1 = Solution()  # Create an instance of the Solution class
    valid_indexes = solution1.twoSum(nums, target)  # Call the twoSum method
    print(valid_indexes)  # Print the result

    print("-"*10)

    nums = [3,2,4]
    target = 6
    solution1 = Solution()  # Create an instance of the Solution class
    valid_indexes = solution1.twoSum(nums, target)  # Call the twoSum method
    print(valid_indexes)  # Print the result


    print("-"*10)

    nums = [3,3]
    target = 6
    solution1 = Solution()  # Create an instance of the Solution class
    valid_indexes = solution1.twoSum(nums, target)  # Call the twoSum method
    print(valid_indexes)  # Print the result



if __name__ == "__main__":
    main()


"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



"""