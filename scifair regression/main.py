# Import scikit learn
from sklearn import datasets

# Load data
iris = datasets.load_iris()
# Print shape of data to confirm data is loaded
print(iris.data.shape)
from sklearn import svm
from sklearn import datasets

# Load dataset
iris = datasets.load_iris()
clf = svm.LinearSVC()
# learn from the data
clf.fit(iris.data, iris.target)
# predict for unseen data
clf.predict([[5.0, 3.6, 1.3, 0.25]])
# Parameters of model can be changed by using the attributes ending with an underscore
print(clf.coef_)

from sklearn import datasets

# Load dataset
iris = datasets.load_iris()
# Create and fit a nearest-neighbor classifier
from sklearn import neighbors

knn = neighbors.KNeighborsClassifier()
knn.fit(iris.data, iris.target)
# Predict and print the result
result = knn.predict([[0.1, 0.2, 0.3, 0.4]])
print(result)
