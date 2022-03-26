import plotly.express as px
import pandas as pd

from google.colab import files
data_to_load=files.upload()

data=pd.read_csv('covid_data.csv')
graph= px.scatter(data, x="date", y="cases",
	          size="cases",color="country",
                   size_max=20)
graph.show()
