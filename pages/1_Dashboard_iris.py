import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import os

st.header("Iris Dataset")

# Reading the data file
CURRDIR = os.path.abspath(os.curdir)
DATA_PATH = os.path.join(CURRDIR, "resources/data/iris.csv")
data = pd.read_csv(DATA_PATH)

st.dataframe(data)

# Boxplot of numerical data
numerical_cols = list(data.select_dtypes(include=[np.number]).columns.values)
fig = px.box(data[numerical_cols])
st.plotly_chart(fig, theme=None, use_container_width=True)

X = st.selectbox("X", data.columns)
Y = st.selectbox("Y", data.columns)

bar_chart, line_chart, scatter_plot = st.tabs(["Bar Chart", "Line Chart", "Scatter Plot"])

if X and Y:
    bar_fig = px.bar(data, x=X, y=X, color=Y)
    line_fig = px.line(data, x=X, y=X, color=Y)
    scatter_fig = px.scatter(data, x=X, y=X, color=Y)

    bar_chart.plotly_chart(bar_fig, theme=None, use_container_width=True)
    line_chart.plotly_chart(line_fig, theme=None, use_container_width=True)
    scatter_plot.plotly_chart(scatter_fig, theme=None, use_container_width=True)
