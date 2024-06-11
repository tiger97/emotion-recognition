import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/tiger/Desktop/tez/multimedia/paper/paper m/data/Emotion_classify_Data.csv')
print(data.head())

# Plot distribution of emotions
sns.countplot(data['Emotion'])
plt.title('Distribution of Emotions')
plt.show()

# Add a new column for text length
data['Text Length'] = data['Comment'].apply(len)

# Plot text length distribution
sns.histplot(data['Text Length'], bins=30)
plt.title('Distribution of Text Sample Lengths')
plt.show()

# Boxplot to show the text lengths for each emotion
sns.boxplot(x='Emotion', y='Text Length', data=data)
plt.title('Text Length by Emotion')
plt.show()

# Create a violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Emotion', y='Text Length', data=data)
plt.title('Distribution of Text Lengths by Emotion')
plt.show()

# library for correlation test
from scipy.stats import spearmanr

# Convert Emotion labels to a numerical format
data['Emotion Code'] = data['Emotion'].astype('category').cat.codes

# Spearman's correlation
correlation, p_value = spearmanr(data['Text Length'], data['Emotion Code'])
print(f'Spearman correlation between text length and emotion: {correlation:.2f}')
print(f'P-value: {p_value:.4f}')

