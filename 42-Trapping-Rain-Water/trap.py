class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l_wall = r_wall = 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        for i in range(len(height)):
            max_left[i] = l_wall
            l_wall = max(l_wall, height[i])
        
        for j in range(len(height) - 1, -1, -1):
            max_right[j] = r_wall
            r_wall = max(r_wall, height[j])
        
        water = 0
        for i in range(len(height)):
            potential_water = min(max_left[i], max_right[i])
            water += max(0, potential_water - height[i])
        return water

solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
print(solution.trap([4,2,0,3,2,5]))  # Output: 9