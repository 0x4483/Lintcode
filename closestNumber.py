class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def closestNumber(self, A, target):
        left = 0
        right = len(A) - 1
        while (left + 1 < right):
            mid = (left + right) / 2 
            if (target < A[mid]):
                right = mid
            else:
                left = mid          
        if (target - A[left] < A[right] - target):
            return left
        else:
            return right

# Time: O(log(n)) 
# Space: O(1) 
# Tag: Binary Search, Easy
