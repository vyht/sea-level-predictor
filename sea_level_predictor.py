import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    plt.clf()
    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = pd.Series(range(int(df['Year'].min()), 2051))
    y_all = res_all.slope * x_all + res_all.intercept
    ax.plot(x_all, y_all)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_2000 = pd.Series(range(2000, 2051))
    y_2000 = res_2000.slope * x_2000 + res_2000.intercept
    ax.plot(x_2000, y_2000)

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
