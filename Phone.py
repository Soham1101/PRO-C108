import pandas as pd
import plotly.express as px
import csv
import numpy
from collections import Counter
import random 
import plotly.figure_factory as ff

df = pd.read_csv("PhoneRatings.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()],["Average Rating"],show_hist = True)
fig.show()
