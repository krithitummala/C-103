import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.bar(df, x="InternetUsers", y="Per capita", color="Country", title ="Bar graph")
fig.show()