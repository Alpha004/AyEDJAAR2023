import math
import sys

DIMENSIONS = 2

class Node:
    def __init__(self, pos, left, right):
        self.position = pos
        self.left_child = left
        self.right_child = right    
    def __str__(self):
        return f"Nodo posicion: {self.position}"

def distance_squared(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = x1 - x2
    dy = y1 - y2
    return dx * dx + dy * dy

def closer_distance(point, pos0, pos1):
    if pos0 is None:
        return pos1
    if pos1 is None:
        return pos0
    dist0 = distance_squared(point, pos0)
    dist1 = distance_squared(point, pos1)

    if dist0 < dist1:
        return pos0
    else:
        return pos1
    
def nearest_neighbor(root, point, nivel=0):
    if root is None:
        return None
    axis = nivel % DIMENSIONS
    next_branch = None
    other_branch = None
    if point[axis] < root.position[axis]:
        next_branch = root.left_child
        other_branch = root.right_child
    else:
        next_branch = root.right_child
        other_branch = root.left_child
    best = closer_distance(point,
                           nearest_neighbor(next_branch,
                                                point,
                                                nivel + 1),
                           root.position)
    if distance_squared(point, best) > (point[axis] - root.position[axis]) ** 2:
        best = closer_distance(point,
                               nearest_neighbor(other_branch,
                                                    point,
                                                    nivel + 1),
                               best)
    return best



def kdtree(points, nivel=0):
    size = len(points)
    if size <= 0:
        return None
    axis = nivel % DIMENSIONS
    sorted_points = sorted(points, key=lambda point: point[axis])
    pos = sorted_points[size // 2]
    return Node(pos,
                kdtree(sorted_points[:size // 2], nivel + 1),
                kdtree(sorted_points[size // 2 + 1:], nivel + 1))



if __name__ == '__main__':

    #LIST_POINTS = [(2,15),(4,8),(12,15),(9,9),(10,4),(14,2),(13,12)]
    LIST_POINTS = [(645.48749, 502.83917),(852.56873, 677.59558),(1096.0155, 661.43311),(1494.0156, 590.72247),(510.12704, 321.01172),(545.48236, 146.25533),(63.63961, 144.23502),(358.60416, 654.36206),(222.23357, 385.66147),(222.23357, 385.66147),(1043.4875, 168.47868),(803.07129, 323.03201)]
    result = kdtree(LIST_POINTS)
    to_found_point = (953.58398, 382.63101)
    found = nearest_neighbor(result, to_found_point)
    found_distance = math.sqrt(distance_squared(to_found_point, found))

    print("Encontrado: %s - distancia: %f" % (found, found_distance))