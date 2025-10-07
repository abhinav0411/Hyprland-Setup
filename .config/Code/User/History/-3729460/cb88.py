import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

df = pd.read_feather("semeion.feather")
print("DataFrame shape:", df.shape)

X = df.iloc[:, :-10]
y = df.iloc[:, -10:].values.argmax(axis=1)
print("Features shape:", X.shape)
print("Labels shape:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

if X_train.size == 0 or y_train.size == 0:
    print("Error: Training data is empty. Check feather file and slicing.")
else:
    svm_rbf = SVC(kernel='rbf', gamma='scale')
    svm_rbf.fit(X_train, y_train)
    y_pred = svm_rbf.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")