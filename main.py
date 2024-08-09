def closest_pair(points):
    def distance(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def brute_force(points):
        min_dist = float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if distance(points[i], points[j]) < min_dist:
                    min_dist = distance(points[i], points[j])
        return min_dist

    def strip_closest(strip, d):
        min_dist = d
        strip.sort(key=lambda point: point[1])
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
                min_dist = min(min_dist, distance(strip[i], strip[j]))
                j += 1
        return min_dist

    def closest_pair_rec(points_sorted_x, points_sorted_y):
        if len(points_sorted_x) <= 3:
            return brute_force(points_sorted_x)

        mid = len(points_sorted_x) // 2
        Qx = points_sorted_x[:mid]
        Rx = points_sorted_x[mid:]

        midpoint = points_sorted_x[mid][0]
        Qy = list(filter(lambda point: point[0] <= midpoint, points_sorted_y))
        Ry = list(filter(lambda point: point[0] > midpoint, points_sorted_y))

        d1 = closest_pair_rec(Qx, Qy)
        d2 = closest_pair_rec(Rx, Ry)
        d = min(d1, d2)

        strip = [point for point in points_sorted_y if abs(point[0] - midpoint) < d]
        d_strip = strip_closest(strip, d)

        return min(d, d_strip)

    points_sorted_x = sorted(points, key=lambda point: point[0])
    points_sorted_y = sorted(points, key=lambda point: point[1])
    return closest_pair_rec(points_sorted_x, points_sorted_y)


# Example usage
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(f"The smallest distance between any two points is: {closest_pair(points)}")
