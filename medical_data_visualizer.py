import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = df["overweight"] = df["weight"] / ((df["height"] / 100) ** 2)

df.loc[df["overweight"] <= 25, "overweight"] = int(0)
df.loc[df["overweight"] > 25, "overweight"] = int(1)
df["overweight"] = df["overweight"].astype("int")

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1,
# make the value 0. If the value is more than 1, make the value 1.

df.loc[df["gluc"] < 2, "gluc"] = 0

df.loc[df["gluc"] >= 2, "gluc"] = 1

df.loc[df["cholesterol"] < 2, "cholesterol"] = 0

df.loc[df["cholesterol"] >= 2, "cholesterol"] = 1


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

    # Draw the catplot with 'sns.catplot()'

    # Get the figure for the output

    df_cat = pd.melt(df, id_vars=["cardio"],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index=False).value_counts()

    fig = sns.catplot(data=df_cat, x="variable", y="count", hue="value", kind="bar", col="cardio")

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data

    df.drop(df[df["ap_hi"] < df["ap_lo"]].index, inplace=True)
    df.drop(df[df['height'] < df['height'].quantile(0.025)].index, inplace=True)
    df.drop(df[df['height'] > df['height'].quantile(0.975)].index, inplace=True)
    df.drop(df[df['weight'] < df['weight'].quantile(0.025)].index, inplace=True)
    df.drop(df[df['weight'] > df['weight'].quantile(0.975)].index, inplace=True)

    df_heat = df

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(data=corr, mask=mask)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig


draw_cat_plot()
draw_heat_map()
