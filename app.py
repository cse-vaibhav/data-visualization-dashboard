import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

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
    fig, ax = plt.subplots(1, 1)
    ax.boxplot(dataframe[numerical_cols], notch=True, vert=False, labels=numerical_cols)
    box_plot.pyplot(fig)
        


if X and Y and dataframe is not None:

    bar_chart_fig, bar_chart_ax = plt.subplots(1, 1)
    bar_chart_ax.bar(dataframe[X], dataframe[Y])
    bar_chart_ax.set_xlabel(X)
    bar_chart_ax.set_ylabel(Y)
    bar_chart.pyplot(bar_chart_fig)

    line_chart_fig, line_chart_ax = plt.subplots(1, 1)
    line_chart_ax.plot(dataframe[X], dataframe[Y])
    line_chart_ax.set_xlabel(X)
    line_chart_ax.set_ylabel(Y)
    line_chart.pyplot(line_chart_fig)

    scatter_plot_fig, scatter_plot_ax = plt.subplots(1, 1)
    scatter_plot_ax.scatter(dataframe[X], dataframe[Y])
    scatter_plot_ax.set_xlabel(X)
    scatter_plot_ax.set_ylabel(Y)
    scatter_plot.pyplot(scatter_plot_fig)

# temp_data_file = DATA_DIR + "tmp.csv"


