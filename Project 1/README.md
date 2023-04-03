# Beverage Manufacturing Company - Red Wine Inventory Analysis
### Introduction
As a data analyst for a beverage manufacturing company, the production department has provided a dataset of all inventories of red wine in a csv file format named data.csv. The aim of this analysis is to perform exploratory data analysis on the dataset and present the findings to the investors in the end of year meeting.

### Data Pre-processing
Before analyzing the data, it is essential to pre-process the dataset to eliminate any null values or duplicates. The method used to handle null values is to remove any rows with null values since the dataset has a large number of rows. The dropna() function in pandas is used to remove rows with null values. Duplicates are also removed using the drop_duplicates() function in pandas.


``` python
import pandas as pd

# Reading csv file
df = pd.read_csv("data.csv")

# Dropping null values
df.dropna(inplace=True)

# Dropping duplicates
df.drop_duplicates(inplace=True)
```

### Statistical Inferences of the Entire Dataset
After pre-processing the data, it is crucial to get an overview of the statistical inferences of the entire dataset. The describe() function in pandas provides a summary of the dataset's statistics, including the mean, standard deviation, minimum, maximum, and quartiles.

``` python
# Summary statistics of the entire dataset
df.describe()
```

### Statistical Inferences of Individual Columns in the Dataset
Apart from the summary statistics of the entire dataset, it is also important to analyze the statistics of individual columns in the dataset. The describe() function can be used for each column by selecting the column using indexing.

``` python
# Summary statistics of individual columns
print(df['column_name'].describe())
```

### Hidden Inferences
There might be some hidden inferences that can be obtained by analyzing the dataset. For instance, the company may want to know the number of bottles of red wine that have been sold or the revenue generated from the sales. The groupby() function in pandas can be used to group the data by a particular column and then compute statistics on the groups.

``` python
# Grouping by column and computing statistics
print(df.groupby('column_name').sum())
```

### Data Correlation Among Columns
To determine if there is a correlation between columns in the dataset, a correlation matrix can be created using the corr() function in pandas. The correlation matrix can then be visualized using a heatmap.

``` python
import seaborn as sns

# Correlation matrix
corr_matrix = df.corr()
# Heatmap of correlation matrix
sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu")
```

### Conclusion
In conclusion, this analysis has provided insight into the inventory of red wine in the beverage manufacturing company. The statistical inferences of the dataset, individual columns, hidden inferences, and data correlation among columns have been analyzed. By analyzing this dataset, the company can make informed decisions about their inventory of red wine.