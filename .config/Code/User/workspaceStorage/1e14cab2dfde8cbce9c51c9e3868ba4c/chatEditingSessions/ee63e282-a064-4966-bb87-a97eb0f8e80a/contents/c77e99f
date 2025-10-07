import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

df = pd.read_feather("semeion.feather")

X = df.iloc[:, :-10]
y = df.iloc[:, -10:].values.argmax(axis=1)  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

svm_rbf = SVC(kernel='rbf', gamma='scale')
svm_rbf.fit(X_train, y_train)
y_pred = svm_rbf.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")