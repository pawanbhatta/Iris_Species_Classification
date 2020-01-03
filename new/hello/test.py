import joblib
import pandas as pd

file_new = open('model.pkl', 'rb')
model = joblib.load('model.pkl')

print(model.predict([[6, 2.9, 5, 1.5]]))
# print(species)
