# Closest Pair Problem

The solution to the Closest Pair Problem using a Divide and Conquer algorithm. For a small number of points (3 or fewer), it uses a brute-force approach. It divides the points into two halves, Q and R, based on their x-coordinates. Recursively finds the closest pairs in Q and R. Determines if there's a closer pair that straddles the two halves.

The algorithm's time complexity is O(nlogn)

### Dependencies

* Python 3.12
