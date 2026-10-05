class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # --- ALGORITHM BLUEPRINT ---
        # 1. Area Formula: width (r - l) * height (the shorter line, to prevent spilling).
        # 2. Start with pointers at the very edges to get the maximum possible width.
        # 3. Key Insight: Moving a pointer inward ALWAYS shrinks the width. 
        #    To find a bigger area, we MUST find a taller line to compensate.
        #    Therefore, always abandon the shorter line! 
        l, r = 0, len(heights) - 1
        max_area = 0
        
        while l < r:
            # The water level is bottlenecked by the shorter of the two lines
            area = min(heights[l],heights[r]) * (r - l)
            max_area = max(max_area, area)

            # Move the pointer with the smaller height, hoping to find a taller one
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
