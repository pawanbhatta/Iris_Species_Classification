from django.db import models
import pandas as pd
import joblib
# Create your models here.


class IrisPlants(models.Model):
    length_petal = models.FloatField()
    length_sepal = models.FloatField()
    width_petal = models.FloatField()
    width_sepal = models.FloatField()
    species = models.IntegerField(
        choices=((0, "Setosa"), (1, "Versicolor"), (2, "Virginica"),))

    # def get_species(self):
    #     self.save()
    # return get_species_display()

    # def __init__(self):
    #     file = pd.open('model.pkl')
    #     species = file.predict()
    #     file.close()
