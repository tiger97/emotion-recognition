import pandas as pd

data = pd.read_csv('C:/Users/tiger/Desktop/tez/multimedia/paper/paper m/data/fear_subset.csv')
print(data.head())

data['Text Length'] = data['Comment'].apply(len)

# Calculate descriptive statistics
descriptive_stats = data['Text Length'].describe()
print("Descriptive Statistics for Joy:", descriptive_stats)

