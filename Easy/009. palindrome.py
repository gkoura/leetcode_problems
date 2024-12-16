class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        if x == 0: return True
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # If the number of digits is odd, we can ignore the middle digit
        return x == reversed_half or x == reversed_half // 10


        



def main():
    x = 10
    solution = Solution()  # Create an instance of the Solution class
    print(solution.isPalindrome(x))


if __name__ == "__main__":
    main()


"""
Given an integer x, return true if x is a 
palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""