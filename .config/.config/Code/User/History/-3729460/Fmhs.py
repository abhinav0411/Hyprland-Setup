from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

data = datasets.load_files("semeion.feather")
X = data.data      
y = data.target    

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an SVM classifier with RBF kernel
svm_rbf = SVC(kernel='rbf', gamma='scale')  # 'scale' is a good default for gamma

# Train the model
svm_rbf.fit(X_train, y_train)

# Predict on the test set
y_pred = svm_rbf.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy with RBF kernel: {accuracy:.2f}")
