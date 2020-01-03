import pickle
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import joblib
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

flower_data = pd.read_csv('iris.csv')
print(flower_data.shape)
print(flower_data.head())

set_of_flowers = set(flower_data['species'])
print(set_of_flowers)

set_of_data = flower_data.iloc[:, :-1].values
# print(set_of_data)
result = flower_data.species
# print(result)


lEnc = LabelEncoder()
result = lEnc.fit_transform(result)
# print(result)
encoder = OneHotEncoder(categories='auto')
encoder.fit_transform(result.reshape(-1, 1)).toarray()
# print(result)

# from sklearn.preprocessing import StandardScaler
# # Normalizing the datas for accurate prediction
# sc = StandardScaler()
# sc.fit(set_of_data)
# scaled_data = sc.transform(set_of_data)
# print(scaled_data[:5,:])


data_train, data_test, result_train, result_test = train_test_split(
    set_of_data, result, test_size=.3, random_state=0)
# print(result_test)


model = KNeighborsClassifier(n_neighbors=7)
model.fit(data_train, result_train)
prediction = model.predict(data_test)
accuracy = accuracy_score(result_test, prediction)

print("Accuracy of KNN :: ", accuracy)
print(model.predict_proba([[6, 2.9, 4.5, 1.5]]))
print(model.predict([[6, 2.9, 5, 1.5]]))
# sepal length,width petal length,width

joblib.dump(model, "iris_pkl_1.pkl")

# knnPickle = open('knnpickle_file.pkl', 'wb')

# pickle.dump(model, knnPickle)

# file = open('knnpickle_file.pkl', 'rb')
# loaded_model = pickle.load(file)
# result = file.predict([[2, 4, 7, 5]])
# print(result)

# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import r2_score
