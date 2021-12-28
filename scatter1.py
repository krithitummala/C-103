import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df, x="Country", y="Per capita", color="Population", title= 
"Scatter Graph", size="Per capita", size_max=40)
fig.show()