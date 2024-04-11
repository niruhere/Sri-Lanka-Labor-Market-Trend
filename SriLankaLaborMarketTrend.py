import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from sklearn.pipeline import Pipeline

st.title("Sri Lanka's Labor Market Trend")

df = pd.read_csv('https://raw.githubusercontent.com/niruhere/Sri-Lanka-Labor-Market-Trend/main/ILOSTAT_SriLanka_LabourMarketTrenddata.csv')
print ("Dataset Length: ", len(df))
print ("Dataset Shape: ", df.shape)
# Remove unwanted columns "Country" and "Source" from the data
df.drop(['Country', 'Source'], axis=1, inplace=True)

# Remove rows having null values(removes 38 out of 1314 records)
df.dropna(axis=0, inplace=True)

# Rename column "Area type" to "Sector", "Sex" to Gender
df.rename(columns = {'Area type':'Sector', 'Sex': 'Gender'}, inplace = True)

st.subheader('Labor Force Participation Rate in %'' for Gender, Education level and Sector')
st.write(df)
# st.subheader('Labour Force Participation rate (LFPR%) by Gender, Sector at different Education Level')

# Set up the layout
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(14, 7))
fig = px.density_heatmap(df.loc[(df.Gender != "Total") & ((df.Sector.str.contains("Rural")) | (df.Sector.str.contains("Urban"))) & (df.Education.str.contains("Aggregate levels"))], x="Year", y="Education", nbinsx=10,  z="Value", facet_row="Gender", facet_col="Sector", histfunc="avg", labels={'Value': 'LFPR%'}, text_auto=True)
fig.update_layout(title="Labour Force Participation rate(LFPR%) by Gender and Sector at the Aggregate Education Level",
                  xaxis_title="Year",
                  yaxis_title="Aggregate Education level")
st.plotly_chart(fig)