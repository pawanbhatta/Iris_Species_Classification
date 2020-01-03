from django.shortcuts import render, redirect
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import json
from django.db.models import Count, Q
from .models import IrisPlants
import pickle
import joblib

# Create your views here.


def home(request):
    if request.method == 'POST':

        # The below code is only to input the data from dataset into the database,,, dont use this code again unless until required
        # iris = pd.read_csv("iris.csv")

        # for i in range(len(iris['species'])):
        #     if iris['species'][i] == 'setosa':
        #         species = 0
        #     elif iris['species'][i] == 'versicolor':
        #         species = 1
        #     else:
        #         species = 2
        #     iris_instance = IrisPlants.objects.create(
        #         length_petal=iris['petal_length'][i], length_sepal=iris['sepal_length'][i], width_petal=iris['petal_width'][i], width_sepal=iris['sepal_width'][i], species=species)
        #     iris_instance.save()

        length_petal = request.POST['petal_length']
        length_sepal = request.POST['sepal_length']
        width_petal = request.POST['petal_width']
        width_sepal = request.POST['sepal_width']

        # model_file = open('hello/model.pkl', 'rb')

        # with open('hello/model.pkl', 'rb') as f:
        #     x = pickle.load(f)
        # loaded_model = pickle.load(open('hello/model.pkl', 'rb'))
        # loaded_model = joblib.load('hello/iris_pkl_1.pkl')

        file1 = open('hello/iris_pkl_1.pkl', 'rb')
        loaded_model = joblib.load(file1)
        print(loaded_model.predict([[6, 2.9, 5, 1.5]]))

        species = loaded_model.predict(
            [[length_sepal, width_sepal, length_petal, width_petal]])
        # x.close()

        iris_instance = IrisPlants.objects.create(
            length_petal=length_petal, length_sepal=length_sepal, width_petal=width_petal, width_sepal=width_sepal, species=species)

        iris_instance.save()

        obj = IrisPlants.objects.get(length_petal=length_petal, length_sepal=length_sepal,
                                     width_petal=width_petal, width_sepal=width_sepal, species=species)

        return render(request, 'home.html', {"iris": obj})

    else:
        return render(request, "home.html")


def chart(request):
    iris = pd.read_csv("iris.csv")
    print(iris.shape)
    value_counts = iris['species'].value_counts()
    sepal_lengths = iris['sepal_length']
    sepal_widths = iris['sepal_width']

    lists = []
    for i in range(len(sepal_lengths)):
        lists.append([sepal_lengths[i], sepal_widths[i]])

    setosa = list()
    virginica = list()
    versicolor = list()

    setosa_num = 0
    versicolor_num = 0
    virginica_num = 0

    for i in range(len(iris['species'])):
        if ((iris['species'][i]) == 'setosa'):
            setosa_num += 1
        if ((iris['species'][i]) == 'versicolor'):
            versicolor_num = versicolor_num + 1
        if ((iris['species'][i]) == 'virginica'):
            virginica_num = virginica_num + 1

    setosa.append(setosa_num)
    versicolor.append(versicolor_num)
    virginica.append(virginica_num)

    categories = list()
    categories.append('species')
# why this shit does not append string

    print(setosa)
    print(versicolor)
    print(virginica)
    print(categories)

    return render(request, 'chart.html', {
        'categories': json.dumps(categories),
        'setosa': json.dumps(setosa),
        'virginica': json.dumps(virginica),
        'versicolor': json.dumps(versicolor)})
