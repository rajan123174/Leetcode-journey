from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells):
        def canCross(day):
            grid = [[0] * col for _ in range(row)]
            
            # Flood cells up to 'day'
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1
            
            queue = deque()
            visited = [[False] * col for _ in range(row)]
            
            # Start BFS from top row
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    visited[0][c] = True
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while queue:
                r, c = queue.popleft()
                
                if r == row - 1:
                    return True
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col:
                        if not visited[nr][nc] and grid[nr][nc] == 0:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
            
            return False
        
        left, right = 0, len(cells)
        
        while left < right:
            mid = (left + right + 1) // 2
            if canCross(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
