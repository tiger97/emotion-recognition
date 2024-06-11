import pandas as pd
import scipy.stats as stats


data = pd.read_csv('C:/Users/tiger/Desktop/tez/multimedia/paper/paper m/data/Emotion_classify_Data.csv')

data['Text Length'] = data['Comment'].apply(len)

# Kruskal-Wallis H-test
kw_test = stats.kruskal(data[data['Emotion'] == 'anger']['Text Length'],
                        data[data['Emotion'] == 'joy']['Text Length'],
                        data[data['Emotion'] == 'fear']['Text Length'])

print("Kruskal-Wallis H-test results:", kw_test)

# Quantile Analysis
quantiles = data.groupby('Emotion')['Text Length'].quantile([0.25, 0.5, 0.75])
print("Quantiles of Text Length for Each Emotion:\n", quantiles)
