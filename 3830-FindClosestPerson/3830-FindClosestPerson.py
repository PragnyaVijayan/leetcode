# Last updated: 9/4/2025, 1:28:09 AM
class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """

        distance_x_z = abs(z-x)
        distance_y_z = abs(z-y)

        if distance_x_z < distance_y_z:
            return 1
        elif distance_y_z < distance_x_z:
            return 2
        else:
            return 0
        

        