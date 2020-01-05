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

        length_petal = request.POST['petal_length']
        length_sepal = request.POST['sepal_length']
        width_petal = request.POST['petal_width']
        width_sepal = request.POST['sepal_width']

        file1 = open('hello/iris_pkl_1.pkl', 'rb')
        loaded_model = joblib.load(file1)

        species = loaded_model.predict(
            [[length_sepal, width_sepal, length_petal, width_petal]])[0]

        iris_instance = IrisPlants.objects.create(
            length_petal=length_petal, length_sepal=length_sepal, width_petal=width_petal, width_sepal=width_sepal, species=species)

        return render(request, 'home.html', {"iris": iris_instance})

    else:
        return render(request, 'home.html')


def chart(request):
    iris = pd.read_csv("iris.csv")
    print(iris.shape)
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

    return render(request, 'chart.html', {
        'categories': json.dumps(categories),
        'setosa': json.dumps(setosa),
        'virginica': json.dumps(virginica),
        'versicolor': json.dumps(versicolor)})
