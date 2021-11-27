import pandas as pd
import plotly.figure_factory as ff
import statistics as stat

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Mobile Brand"])
fig.show()
