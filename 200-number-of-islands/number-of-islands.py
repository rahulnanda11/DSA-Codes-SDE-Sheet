class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        result=0

        def dfs(i,j):
            if i>=m or j>=n or i<0 or j<0 or grid[i][j]=="0":
                return 0
            else:
                grid[i][j]="0"
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)
        
        for row in range(m):
            for col in range(n):
                if grid[row][col]=="1":
                    dfs(row,col)
                    result+=1
        return result
        