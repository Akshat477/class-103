import pandas as pn 
import plotly.express as pe 

file =  pn.read_csv("line_chart.csv")
fig  = pe.line(file,x = "Year",y = "Per capita income", color = "Country",title = "Per capita income")
fig.show()