class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_list=[num**2 for num in nums]
        square_list.sort()
        return square_list