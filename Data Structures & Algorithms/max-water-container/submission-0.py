class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # height of smaller container * distance between them = area
        max_area = 0
        for i, h1 in enumerate(heights):
            for j, h2 in enumerate(heights):
                if i == j: continue
                smaller_height = h1 if h1 < h2 else h2
                area = smaller_height * abs(j - i)
                max_area = area if area > max_area else max_area
        return max_area



