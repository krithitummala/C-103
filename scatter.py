import pandas as pd
import plotly.express as px

df = pd.read_csv("line_chart.csv")
fig = px.scatter(df, x="Year", y="Per capita income", color="Country", title="Scatter Graph", size="Per capita income", size_max=40)
fig.show()