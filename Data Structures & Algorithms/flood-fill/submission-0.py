class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        arr = []
        adj= [[0,1],[1,0],[0,-1],[-1,0]]
        row, cols = len(image), len(image[0])
        origin = image[sr][sc]
        
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=cols or image[r][c]==color:
                return
            if image[r][c]==origin:
                image[r][c]=color
                for dr, dc in adj:
                    dfs(r+dr,c+dc)


        for r in range(row):
            for c in range(cols):
                if r==sr and c==sc:
                    dfs(r,c)
                    


        return image