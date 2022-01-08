import pandas as pn
import plotly.express as pe 

Data = pn.read_csv("data.csv")
Graph = pe.bar(Data,x = "Country", y = "InternetUsers")
Graph.show()