class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # height of smaller container * distance between them = area


        low = 0
        high = len(heights) - 1
        max_area = 0
        while low < high:
            h1 = heights[low]
            h2 = heights[high]
            smaller_height = h1 if h1 < h2 else h2
            area = smaller_height * abs(high - low)
            max_area = area if area > max_area else max_area
            if h1 < h2:
                low+=1
            else: 
                high-=1
        return max_area


