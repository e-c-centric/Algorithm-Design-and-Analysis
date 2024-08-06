<<<<<<< HEAD
import math


def closest_pair(x:list, y: list) -> tuple:
    """
    Finds the closest pair of points in a given set of points.

    The function takes two parameters, x and y, which represent the list of points sorted by their x-coordinates and y-coordinates respectively. The points are typically represented as tuples or objects with x and y attributes.

    The algorithm starts by recursively dividing the set of points into smaller subsets. This is done by finding the midpoint along the x-axis and splitting the points into two halves based on this midpoint.

    The algorithm then recursively applies itself to the left and right halves of the points until the base case is reached. The base case is when there are only two or three points in a subset. In this case, the algorithm can directly calculate the distance between these points and return the closest pair.

    After the recursive calls, the algorithm merges the results from the left and right halves. It determines the distance between the closest pair found in each half.

    Finally, the algorithm checks for any points that are closer to the dividing line than the minimum distance found so far. This is done by considering a strip of points around the dividing line and comparing their distances to the minimum distance. If a closer pair is found, the minimum distance is updated.

    The algorithm returns the closest pair of points and their distance.

    Args:
        x (list): List of points sorted by x-coordinate.
        y (list): List of points sorted by y-coordinate.

    Returns:
        tuple: A tuple containing the closest pair of points.

    """
    x.sort()

    n = len(x)
    if n <= 3:
        return brute_force(x, y)

    mid = n // 2
    mid_point = x[mid]

    left_x = x[:mid]
    right_x = x[mid:]

    left_y = []
    right_y = []
    for point in y:
        if point[0] <= mid_point[0]:
            left_y.append(point)
        else:
            right_y.append(point)

    left_pair = closest_pair(left_x, left_y)
    right_pair = closest_pair(right_x, right_y)

    min_dist = min(distance(left_pair[0], left_pair[1]), distance(
        right_pair[0], right_pair[1]))

    strip_pair = closest_strip(x, y, mid_point, min_dist)

    return min(left_pair, right_pair, strip_pair, key=lambda pair: distance(pair[0], pair[1]))


def brute_force(x:list, y:list) -> tuple:
    """
    Finds the closest pair of points using a brute force approach.
    The function takes two parameters, x and y, which represent the list of points sorted by their x-coordinates and y-coordinates respectively. The points are typically represented as tuples or objects with x and y attributes.
    
    The algorithm iterates through all pairs of points and calculates the distance between them. It keeps track of the minimum distance found so far and the pair of points that correspond to this distance.

    Args:
        x (list): List of points sorted by x-coordinate.
        y (list): List of points sorted by y-coordinate.

    Returns:
        tuple: A tuple containing the closest pair of points.
    
    """
    min_dist = float('inf')
    pair = None
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            dist = distance(x[i], x[j])
            if dist < min_dist:
                min_dist = dist
                pair = (x[i], x[j])
    return pair


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def closest_strip(x, y, mid_point, min_dist):
    """
    Finds the closest pair of points within a given strip.

    Parameters:
    x (list): List of points sorted by x-coordinate.
    y (list): List of points sorted by y-coordinate.
    mid_point (tuple): The midpoint of the strip.
    min_dist (float): The minimum distance between points.

    Returns:
    tuple: The closest pair of points within the strip.
    """
    strip = []
    for point in y:
        if abs(point[0] - mid_point[0]) < min_dist:
            strip.append(point)

    min_dist = float('inf')
    pair = None
    for i in range(len(strip)):
        for j in range(i+1, min(i+7, len(strip))):
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                pair = (strip[i], strip[j])
    return pair


def main():
    x = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    y = sorted(x, key=lambda point: point[1])

    print(closest_pair(x, y))


if __name__ == "__main__":
    main()
=======
import math


def closest_pair(x:list, y: list) -> tuple:
    """
    Finds the closest pair of points in a given set of points.

    The function takes two parameters, x and y, which represent the list of points sorted by their x-coordinates and y-coordinates respectively. The points are typically represented as tuples or objects with x and y attributes.

    The algorithm starts by recursively dividing the set of points into smaller subsets. This is done by finding the midpoint along the x-axis and splitting the points into two halves based on this midpoint.

    The algorithm then recursively applies itself to the left and right halves of the points until the base case is reached. The base case is when there are only two or three points in a subset. In this case, the algorithm can directly calculate the distance between these points and return the closest pair.

    After the recursive calls, the algorithm merges the results from the left and right halves. It determines the distance between the closest pair found in each half.

    Finally, the algorithm checks for any points that are closer to the dividing line than the minimum distance found so far. This is done by considering a strip of points around the dividing line and comparing their distances to the minimum distance. If a closer pair is found, the minimum distance is updated.

    The algorithm returns the closest pair of points and their distance.

    Args:
        x (list): List of points sorted by x-coordinate.
        y (list): List of points sorted by y-coordinate.

    Returns:
        tuple: A tuple containing the closest pair of points.

    """
    x.sort()

    n = len(x)
    if n <= 3:
        return brute_force(x, y)

    mid = n // 2
    mid_point = x[mid]

    left_x = x[:mid]
    right_x = x[mid:]

    left_y = []
    right_y = []
    for point in y:
        if point[0] <= mid_point[0]:
            left_y.append(point)
        else:
            right_y.append(point)

    left_pair = closest_pair(left_x, left_y)
    right_pair = closest_pair(right_x, right_y)

    min_dist = min(distance(left_pair[0], left_pair[1]), distance(
        right_pair[0], right_pair[1]))

    strip_pair = closest_strip(x, y, mid_point, min_dist)

    return min(left_pair, right_pair, strip_pair, key=lambda pair: distance(pair[0], pair[1]))


def brute_force(x:list, y:list) -> tuple:
    """
    Finds the closest pair of points using a brute force approach.
    The function takes two parameters, x and y, which represent the list of points sorted by their x-coordinates and y-coordinates respectively. The points are typically represented as tuples or objects with x and y attributes.
    
    The algorithm iterates through all pairs of points and calculates the distance between them. It keeps track of the minimum distance found so far and the pair of points that correspond to this distance.

    Args:
        x (list): List of points sorted by x-coordinate.
        y (list): List of points sorted by y-coordinate.

    Returns:
        tuple: A tuple containing the closest pair of points.
    
    """
    min_dist = float('inf')
    pair = None
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            dist = distance(x[i], x[j])
            if dist < min_dist:
                min_dist = dist
                pair = (x[i], x[j])
    return pair


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def closest_strip(x, y, mid_point, min_dist):
    """
    Finds the closest pair of points within a given strip.

    Parameters:
    x (list): List of points sorted by x-coordinate.
    y (list): List of points sorted by y-coordinate.
    mid_point (tuple): The midpoint of the strip.
    min_dist (float): The minimum distance between points.

    Returns:
    tuple: The closest pair of points within the strip.
    """
    strip = []
    for point in y:
        if abs(point[0] - mid_point[0]) < min_dist:
            strip.append(point)

    min_dist = float('inf')
    pair = None
    for i in range(len(strip)):
        for j in range(i+1, min(i+7, len(strip))):
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                pair = (strip[i], strip[j])
    return pair


def main():
    x = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    y = sorted(x, key=lambda point: point[1])

    print(closest_pair(x, y))


if __name__ == "__main__":
    main()
>>>>>>> 9681e1f43439df2f2b411d2e26963757fec5caae
