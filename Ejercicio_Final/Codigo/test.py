import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from math import sqrt
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, classification_report
from matplotlib.colors import ListedColormap
from scipy.spatial import distance



def read_csv(filename):
  with open(filename, "r") as f:
    reader = csv.reader(f)
    next(reader, None)
    data = []
    for row in reader:
      data.append(tuple(row))
    return data

class KNN():
  def __init__(self,k):
    self.k=k
    print(self.k)
  def fit(self,X_train,y_train):
    self.x_train=X_train
    self.y_train=y_train
  def calculate_euclidean(self,sample1,sample2):
    distance_temp=0.0
    for i in range(len(sample1)):
      #distance+=(sample1[i]-sample2[i])**2 #Euclidean Distance = sqrt(sum i to N (x1_i – x2_i)^2)
      distance_temp+=distance.euclidean(sample1,sample2)
    #return sqrt(distance)
    return distance_temp
  def nearest_neighbors(self,test_sample):
    distances=[]#calculate distances from a test sample to every sample in a training set
    for i in range(len(self.x_train)):
      distances.append((self.y_train[i],self.calculate_euclidean(self.x_train[i],test_sample)))
    distances.sort(key=lambda x:x[1])#sort in ascending order, based on a distance value
    neighbors=[]
    for i in range(self.k): #get first k samples
      neighbors.append(distances[i][0])
    return neighbors
  def predict(self,test_set):
    predictions=[]
    for test_sample in test_set:
      neighbors=self.nearest_neighbors(test_sample)
      labels=[sample for sample in neighbors]
      prediction=max(labels,key=labels.count)
      predictions.append(prediction)
    return predictions



if __name__ == '__main__':
    dataset = pd.read_csv('F:/Jesus/UNSA/Maestria/Cursos/AlgoritmosYEstructurasdeDatos/MaestriaAyEDGrupo04/Ejercicio_Final/Data/DataSet/Heart_Attack_3_slim.csv')
    # dataset.iloc[:, 6:8] = dataset.iloc[:, 6:8].astype(float)
    # dataset.iloc[:, 0:5] = dataset.iloc[:, 0:5].astype(int)
    # dataset.iloc[:, 8:9] = dataset.iloc[:, 8:9].astype(int)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    # print(dataset.iloc[:, 8:9].values)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    # print(X)
    # print(y)
    # print(X_train)
    # print(y_train)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test) #avoid data leakage

    print(X_train)
    print(X_test.dtype)

    model=KNN(5) #our model
    model.fit(X_train,y_train)

    classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)#The default metric is minkowski, and with p=2 is equivalent to the standard Euclidean metric.
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    predictions=model.predict(X_test)#our model's predictions

    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    accuracy_score(y_test, y_pred)

    cm = confusion_matrix(y_test, predictions) #our model
    print(cm)
    accuracy_score(y_test, predictions)


    X_set, y_set = sc.inverse_transform(X_test), y_test
    X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 10, stop = X_set[:, 0].max() + 10, step = 1),
                        np.arange(start = X_set[:, 1].min() - 10, stop = X_set[:, 1].max() + 10, step = 1))
    plt.contourf(X1, X2, classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
                alpha = 0.75, cmap = ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())    
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], c = ListedColormap(('red', 'green'))(i), label = j)
    plt.title('K-NN (Test set)')
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.legend()
    plt.show()