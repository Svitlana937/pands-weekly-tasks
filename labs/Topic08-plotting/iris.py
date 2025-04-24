from sklearn.datasets import load_iris

# Load the dataset
iris = load_iris()

# Access the data
print(iris.data)         # Feature values
print(iris.target)       # Target labels
print(iris.feature_names) # Feature names
print(iris.target_names)  # Target class names