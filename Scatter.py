import pandas as pn
import plotly.express as pe

df = pn.read_csv("data.csv")
fig = pe.scatter(df,x="Population",y="Per capita",size = "Percentage",color = "Country",size_max = 60)
fig.show()
