import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df,x = "Population",y="Per capita",size = "Percentage",color = "Country",title = 'Per Capita Income',size_max = 60)
fig.show()