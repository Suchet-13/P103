import pandas as pnd
import plotly.express as px

df = pnd.read_csv("Copy+of+data+-+data.csv")
graph = px.scatter(df, x = "date", y = "cases", color = "country")
graph.show()