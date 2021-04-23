import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sea_df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = sea_df['Year']
    y = sea_df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y, c="b", s=10, alpha=0.5)

    # Create first line of best fit
    sea_stats = linregress(x, y)
    sea_incept = sea_stats.intercept
    sea_slope = sea_stats.slope

    x_line = range(1880, 2050)

    plt.plot(x_line, sea_slope * x_line + sea_incept, color="red")

    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()