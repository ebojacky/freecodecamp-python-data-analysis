import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    fig, axes = plt.subplots(figsize=(15, 10))
    axes.scatter(x, y)

    # Create first line of best fit
    results = linregress(x, y)
    x_predict = pd.Series([i for i in range(1880, 2051)])
    y_predict = results.slope * x_predict + results.intercept

    axes.plot(x_predict, y_predict, "r")

    # Create second line of best fit
    df_new = df[df["Year"] >= 2000]
    x_new = df_new["Year"]
    y_new = df_new["CSIRO Adjusted Sea Level"]

    results_2 = results = linregress(x_new, y_new)
    x_predict_new = pd.Series([i for i in range(2000, 2051)])
    y_predict_new = results_2.slope * x_predict_new + results.intercept

    axes.plot(x_predict_new, y_predict_new, "g")

    # Add labels and title
    axes.set_xlabel("Year")
    axes.set_ylabel("Sea Level (inches)")
    axes.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    plt.show()
    return plt.gca()

draw_plot()