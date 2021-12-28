import pandas as pd
import plotly.express as px

df = pd.read_csv("line_chart.csv")
fig = px.bar(df,x = "Year", y="Per capita income", color="Country", title = "Bar Graph")
fig.show()