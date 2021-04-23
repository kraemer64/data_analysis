import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    sea_df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(20, 10))

    x = sea_df['Year']
    y = sea_df['CSIRO Adjusted Sea Level']

    plt.scatter(x, y)

    # Create first line of best fit
    sea_slope, sea_intercept, r_value, p_value, err = linregress(x, y)

    x_ser = pd.Series([*range(sea_df['Year'][0], 2051)])
    y_ser = sea_intercept + sea_slope * x_ser
    
    plt.plot(x_ser, y_ser)

    # Create second line of best fit
    (sea_slope, sea_intercept, p_value, r_value, err) = linregress(
        sea_df[sea_df['Year'] >= 2000]['Year'], 
        sea_df[sea_df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])

    x_2000 = pd.Series([*range(2000, 2051)])
    y_2000 = sea_intercept + sea_slope * x_2000

    plt.plot(x_2000, y_2000, 'r')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()