# PROJECT 2: DATA CLASSIFICATION USING AI
# Iris Flower Classification using Machine Learning

# Import required libraries
import pandas as pd
import numpy as np

# Dataset
from sklearn.datasets import load_iris

# Train-Test Split
from sklearn.model_selection import train_test_split

# Classification Algorithm
from sklearn.tree import DecisionTreeClassifier

# Evaluation Metrics
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# STEP 1: LOAD DATASET
print("LOADING DATASET")
iris = load_iris()

# Features
X = iris.data

# Labels
y = iris.target

# Create DataFrame for understanding dataset
df = pd.DataFrame(X, columns=iris.feature_names)
df["species"] = y

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nTarget Classes:")
print(iris.target_names)

# STEP 2: UNDERSTAND DATASET
print("DATASET INFORMATION")

print("\nSummary Statistics:")
print(df.describe())

print("\nClass Distribution:")
print(df["species"].value_counts())

# STEP 3: SPLIT DATA

print("TRAIN TEST SPLIT")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# STEP 4: TRAIN MODEL

print("MODEL TRAINING")

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=4,
    random_state=42
)

model.fit(X_train, y_train)

print("Model Training Completed Successfully!")

# STEP 5: MAKE PREDICTIONS

print("PREDICTIONS")

y_pred = model.predict(X_test)

print("Predicted Values:")
print(y_pred)

print("\nActual Values:")
print(y_test)

# STEP 6: EVALUATE MODEL

print("MODEL EVALUATION")

accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy : {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# STEP 7: TEST CUSTOM INPUT

print("CUSTOM PREDICTION")

sample = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(sample)

flower_name = iris.target_names[prediction[0]]

print("Sample Flower Features:")
print(sample)

print("Predicted Flower Species:")
print(flower_name)
