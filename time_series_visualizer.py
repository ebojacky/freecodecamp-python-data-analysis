import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
df = df.drop(df[df["value"] < df["value"].quantile(0.025)].index)
df = df.drop(df[df["value"] > df["value"].quantile(0.975)].index)


def draw_line_plot():
    # Draw line plot

    fig, graph1 = plt.subplots(figsize=(20, 10))
    graph1.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    graph1.set_xlabel("Date")
    graph1.set_ylabel("Page Views")
    graph1.plot(df.index, df["value"], "r", linewidth=2)

    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df["month"] = df.index.month
    df["year"] = df.index.year
    df_bar = df.groupby(["year", "month"]).mean()

    # Draw bar plot

    fig = df_bar.unstack().plot.bar(figsize=(10, 5), xlabel="Years", ylabel="Average Page Views", legend=True)
    plt.legend(
        ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"])
    plt.show()
    # Save image and return fig (don't change this part)
    #fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    df_box["month_num"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_num")

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

    ax1 = sns.boxplot(x=df_box["year"], y=df_box["value"], ax=ax1)
    ax2 = sns.boxplot(x=df_box["month"], y=df_box["value"], ax=ax2)

    ax1.set_title("Year-Wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")

    ax2.set_title("Month-Wise Box Plot (Trend)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    plt.show()
    # Save image and return fig (don't change this part)
    #fig.savefig('box_plot.png')
    return fig


draw_line_plot()
draw_bar_plot()
draw_box_plot()