class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret=[]
        while matrix:
            #1)1st row
            ret+=(matrix.pop(0))
            #2)
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            #3)
            if matrix:
                ret+=(matrix.pop()[::-1])
            #4)
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret
