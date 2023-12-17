import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import sys

# Adapted from https://gist.github.com/zhiyzuo/d38159a7c48b575af3e3de7501462e04
# This script takes a data table in csv format and performs Pearson correlation analysis on two columns
# It then draws a scatter plot of the data from these two columns 

def pearsonr_ci(x, y, alpha=0.05):
    ''' calculate Pearson correlation along with the confidence interval using scipy and numpy
    Parameters
    ----------
    x, y : iterable object such as a list or np.array
      Input for correlation calculation
    alpha : float
      Significance level. 0.05 by default
    Returns
    -------
    r : float
      Pearson's correlation coefficient
    pval : float
      The corresponding p value
    lo, hi : float
      The lower and upper bound of confidence intervals
    '''
    r, p = stats.pearsonr(x, y)
    r_z = np.arctanh(r)
    se = 1/np.sqrt(x.size-3)
    z = stats.norm.ppf(1-alpha/2)
    lo_z, hi_z = r_z-z*se, r_z+z*se
    lo, hi = np.tanh((lo_z, hi_z))
    return r, p, lo, hi

def plot_scatter(x, y, xlabel, ylabel, output_location):
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(output_location)
    plt.close()  # Close the figure to release resources
    print(f"Scatter plot saved to: {output_location}")

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 6:
        print("Usage: python script.py input_csv_file x_column y_column alpha output_image_location")
        sys.exit(1)

    input_csv_file = sys.argv[1]
    x_column = sys.argv[2]
    y_column = sys.argv[3]
    alpha_value = float(sys.argv[4])
    output_image_location = sys.argv[5]

    # Read data from CSV file
    df = pd.read_csv(input_csv_file)
    
    # Extract x and y columns from the DataFrame
    x = df[x_column]
    y = df[y_column]

    # Calculate Pearson correlation and confidence interval
    result = pearsonr_ci(x, y, alpha=alpha_value)
    print("Pearson's correlation coefficient:", result[0])
    print("P-value:", result[1])
    print("Confidence Interval (Lower Bound):", result[2])
    print("Confidence Interval (Upper Bound):", result[3])

    # Plot scatter and save the image
    plot_scatter(x, y, xlabel=f"{x_column}", ylabel=f"{y_column}", output_location=output_image_location)