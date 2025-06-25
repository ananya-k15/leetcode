class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        original = image[sr][sc]
        seen = set()
        def modify_neighbours(i, j):
            if (i, j) in seen:
                return
            seen.add((i, j))
            
            image[i][j] = color
            if i > 0 and image[i-1][j] == original:
                modify_neighbours(i-1, j)
            if j > 0 and image[i][j-1] == original:
                modify_neighbours(i, j-1)
            if i < m-1 and image[i+1][j] == original:
                modify_neighbours(i+1, j)
            if j < n-1 and image[i][j+1] == original:
                modify_neighbours(i, j+1)
        
        modify_neighbours(sr, sc)
        return image
