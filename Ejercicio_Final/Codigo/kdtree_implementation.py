import sys
import csv
from scipy.spatial import distance
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, classification_report

DIMENSIONS = 8
MAX_DIST = 999999999999
MAX_NEIGHBORDS = 5

def read_csv(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        data = []
        for row in reader:
            data.append(tuple(row))
        return data

class Node:
    def __init__(self, pos, left, right):
        self.position = pos
        self.left_child = left
        self.right_child = right    
    def __str__(self):
        return f"Nodo posicion: {self.position}"

class KDTree:
    def __init__(self,k):
        self.k=k
        self.root = None
        

    def fit(self,x_training_data,y_training_data):
        self.x_train=x_training_data
        self.y_train=y_training_data
        self.points = []
        for i in range(len(self.x_train)):
            tmpobj = [(self.y_train[i])]
            tmpobj2 = self.x_train[i].tolist()
            # Arreglar el tema del 'list' object cannot be interpreted as an integer en esta linea 
            tmpobj2.extend(tmpobj)           
            self.points.append(tmpobj2)
        self.root = self.kdtree_build(self.points)
    
    def kdtree_build(self, points, nivel=0):
        size = len(points)
        if size <= 0:
            return None
        axis = nivel % DIMENSIONS
        sorted_points = sorted(points, key=lambda point: point[axis])
        pos = sorted_points[size // 2]
        return Node(pos,
                    self.kdtree_build(sorted_points[:size // 2], nivel + 1),
                    self.kdtree_build(sorted_points[size // 2 + 1:], nivel + 1))
    
    def euclidean_distance(self, node1, node2):
        if len(node2) > len(node1):
            return distance.euclidean(node1,node2[:-1])
        return distance.euclidean(node1,node2)
    
    def find_knn(self, k, root, node):
        neighbors = []
        if root is not None:
            distance = self.euclidean_distance(node.position, root.position)
            neighbors.append((root.position[-1], distance, root))
        if root is None:            
            return []
        else:
        # Vecinos más cercanos izquierda
            left_neighbors = self.find_knn(k, root.left_child, node)
            # Vecinos más cercanos derecha
            right_neighbors = self.find_knn(k - len(left_neighbors), root.right_child, node)
            neighbors.extend(left_neighbors)
            neighbors.extend(right_neighbors)  
            neighbors.sort(key=lambda x: x[1])
        return neighbors[:k]
    
    def predict(self, k, test_set):
        predictions=[]
        for test_sample in test_set:
            neighbors=self.find_knn(k, self.root, Node(test_sample.tolist(),None,None))
            labels= list(map(lambda tupla: tupla[0], neighbors))
            prediction=max(labels,key=labels.count)
            predictions.append(prediction)
        return predictions

    def distance_squared(self,point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        dx = x1 - x2
        dy = y1 - y2
        return dx * dx + dy * dy

    def closer_distance(self,point, pos0, pos1):
        if pos0 is None:
            return pos1
        if pos1 is None:
            return pos0
        dist0 = self.distance_squared(point, pos0)
        dist1 = self.distance_squared(point, pos1)

        if dist0 < dist1:
            return pos0
        else:
            return pos1
        
    def nearest_neighbor(self, root, point, nivel=0):
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
        best = self.closer_distance(point, self.nearest_neighbor(next_branch, point, nivel + 1), root.position)
        if self.distance_squared(point, best) > (point[axis] - root.position[axis]) ** 2:
            best = self.closer_distance(point, self.nearest_neighbor(other_branch, point, nivel + 1), best)
        return best

if __name__ == '__main__':
    args = sys.argv[1:]    
    filename = str(args[0]) if args else 'F:/Jesus/UNSA/Maestria/Cursos/AlgoritmosYEstructurasdeDatos/MaestriaAyEDGrupo04/Ejercicio_Final/Data/DataSet/Heart_Attack_3.csv'
    #LIST_POINTS = [(2,15),(4,8),(12,15),(9,9),(10,4),(14,2),(13,12)]
    #LIST_POINTS = [(645.48749, 502.83917),(852.56873, 677.59558),(1096.0155, 661.43311),(1494.0156, 590.72247),(510.12704, 321.01172),(545.48236, 146.25533),(63.63961, 144.23502),(358.60416, 654.36206),(222.23357, 385.66147),(222.23357, 385.66147),(1043.4875, 168.47868),(803.07129, 323.03201)]
    # LIST_POINTS = read_csv(filename)
    LIST_POINTS = pd.read_csv(filename).convert_dtypes()
    X = LIST_POINTS.iloc[:, :-1].values
    y = LIST_POINTS.iloc[:, -1].values.astype(int)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    print('Shape of X_Train set : {}'.format(X_train.shape))
    print('Shape of y_Train set : {}'.format(y_train.shape))
    print('_'*50)
    print('Shape of X_test set : {}'.format(X_test.shape))
    print('Shape of y_test set : {}'.format(y_test.shape))

    # kdtreeObj = kdtree(X)
    kdtreeObj = KDTree(MAX_NEIGHBORDS)
    kdtreeObj.fit(X_train,y_train)

    print("KDTREE BUILD SUCCESS!!")
    # to_found_point = (953.58398, 382.63101)
    # found = nearest_neighbor(result, to_found_point)
    # found_distance = math.sqrt(distance_squared(to_found_point, found))
    # point_to_find = Node((49,1,59,110,65,149,3.18,0.003,1),None,None)
    # results = kdtreeObj.find_knn(MAX_NEIGHBORDS,kdtreeObj.root,point_to_find)
    print("STARTING THE PREDICTIONS...")
    labels_predictions=kdtreeObj.predict(MAX_NEIGHBORDS,X_test)    
    # labels_predictions = list(map(lambda tupla: tupla[0], predictions))

    print("CLASIFICATION DATA:\n")
    print(y_test)

    print('PREDICTIONS:\n')
    print(labels_predictions)

    cm = confusion_matrix(y_test, labels_predictions) #our model
    print(cm)

    print("ACCURACY: " + str(accuracy_score(y_test, labels_predictions)) + "\n\n")
    print("PRECISION SCORE: " + str(precision_score(y_test, labels_predictions)) + "\n\n")
    print("RECALL: " + str(recall_score(y_test, labels_predictions)) + "\n\n")
    print("F1 : " + str(f1_score(y_test, labels_predictions)) + "\n\n")
    print(classification_report(y_test, labels_predictions))
    # print("Encontrado: %s - distancia: %f" % (found, found_distance))

    # YELLOW = 0, PURPLE = 1, BLUE = TO CLASSIFY
    plt.scatter(X_train[:,0], X_train[:,5], c= y_train)
    plt.scatter(X_test[0,0], X_test[0,5], s=120)
    plt.grid()
    plt.show()
