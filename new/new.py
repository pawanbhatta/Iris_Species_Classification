import joblib
import pandas as pd

file1 = open('iris_pkl_1.pkl', 'rb')
model1 = joblib.load(file1)
print(model1.predict([[6, 2.9, 5, 1.5]]))
