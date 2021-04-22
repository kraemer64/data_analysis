import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_ecamination.csv')

# Add 'overweight' column
df['overweight'] = ((df['weight'] / (df['height'] / 100) ** 2) > 25).replace([True, False], [1, 0])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
medical_norm_dict = { 1: 0, 2 : 1, 3: 1}
df['cholesterol'] = df['cholesterol'].map(medical_norm_dict)
df['gluc'] = df['gluc'].map(medical_norm_dict)
print(df.head(10), '\n')

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(
        frame=df, 
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], 
        id_vars=['cardio']
    )

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(
        df_cat.groupby(['variable', 'value', 'cardio'])['value'].count()).rename(
        columns={'value': 'total'}).reset_index()

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(x='variable', y='total', hue='value', 
        col='cardio', data=df_cat, kind='bar')

    # Do not modify the next two lines
    plt.savefig('catplot.png')
    return plt


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, linewidths=.5, annot=True, mask=mask, square=True, 
        vmax=.3, center=0, fmt='.1f', cbar_kws={"shrink": .5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
    