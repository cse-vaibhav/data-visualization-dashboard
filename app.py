import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

st.header("Data Visualization App")

# Sidebar
sidebar = st.sidebar

# receive a data file from user
sidebar.write("## Upload a Data File")
uploaded_file = sidebar.file_uploader("", type=["csv"])
dataframe = None

# x and y columns for plotting
X = None
Y = None
if uploaded_file:
    dataframe = pd.read_csv(uploaded_file)
    st.header("Data")
    st.dataframe(dataframe, use_container_width=True)

    X = st.selectbox("X", dataframe.columns)
    Y = st.selectbox("Y", dataframe.columns)

    bar_chart, line_chart, scatter_plot, box_plot = st.tabs(["Bar Chart", "Line Chart", "Scatter Plot", "Box Plot"])

if dataframe is not None:
    numerical_cols = list(dataframe.select_dtypes(include=[np.number]).columns.values)
    fig = px.box(dataframe[numerical_cols])
    box_plot.plotly_chart(fig, theme=None, use_container_width=True)
        


if X and Y and dataframe is not None:

    bar_fig = px.bar(dataframe, x=X, y=Y, color=Y)
    bar_chart.plotly_chart(bar_fig, theme=None, use_container_width=True)

    line_fig = px.line(dataframe, x=X, y=Y, color=Y)
    line_chart.plotly_chart(line_fig, theme=None, use_container_width=True)

    scatter_fig = px.scatter(dataframe, x=X, y=Y, color=Y)
    scatter_plot.plotly_chart(scatter_fig, theme=None, use_container_width=True)

# temp_data_file = DATA_DIR + "tmp.csv"


