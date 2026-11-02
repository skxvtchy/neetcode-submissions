class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows, cols = len(image), len(image[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        origin = image[sr][sc]

        def dfs(r,c):
            if r>rows-1 or c>cols-1 or r<0 or c<0 or image[r][c]==color:
                return
            print(r,c)
            # print(origin)
            # image[r,c]
            if image[r][c]!=origin:
                return
            image[r][c]=color

            for dr, dc in directions:
                dfs(r+dr,c+dc)
                # image[r][c]=color



        for r in range(rows):
            for c in range(cols):
                if r==sr and c==sc:
                    dfs(r,c)
                    break

        return image