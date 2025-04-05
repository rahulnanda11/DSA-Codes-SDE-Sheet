class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m,n=len(matrix),len(matrix[0])
        low,high=0,m*n-1

        while low<=high:
            mid=(low+high)//2
            row,col=divmod(mid,n)
            mid_val=matrix[row][col]

            if mid_val==target:
                return True
            elif mid_val<target:
                low=mid+1
            else:
                high=mid-1
        return False
