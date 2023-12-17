# Statistical Analysis Repository

Welcome to the Statistical Analysis Repository! This repository contains scripts for conducting statistical analyses on datasets. The primary goal is to provide a flexible tool for researchers and data analysts to perform statistical assessments on their datasets.

## Overview

The repository includes a Python script (`PearsonR.py`) that calculates Pearson's correlation coefficient, p-value, and confidence intervals for two columns of a CSV file. The script also generates a scatter plot of the data and saves it as an image file.

## Getting Started

### Prerequisites

- Python 3.10.12
- Required Python packages: `pandas`, `numpy`, `scipy`, `matplotlib`

Install the necessary packages using the following command:

```bash
pip install pandas numpy scipy matplotlib
```

### Usage

#### Example

Using the pokemon.csv dataset from Kaggle https://www.kaggle.com/datasets/abcsds/pokemon we can test the correlation between the 'attack' and 'defense' attributes

| Statistic                         | Value             |
| --------------------------------- | ----------------- |
| Pearson's correlation coefficient | 0.4386870551184896 |
| P-value | 15.8584798642888974e-39 |
| Confidence Interval (Lower Bound) | 0.3809567323907725 |
| Confidence Interval (Upper Bound) | 0.49301014457787573 |


