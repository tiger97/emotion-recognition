import pandas as pd

data = pd.read_csv('C:/Users/tiger/Desktop/tez/multimedia/paper/paper m/data/Emotion_classify_Data.csv')

print(data.columns)

data['Text Length'] = data['Comment'].apply(len)

mean_length = data['Text Length'].mean()
std_dev = data['Text Length'].std()
min_length = data['Text Length'].min()
max_length = data['Text Length'].max()

print("Mean Text Length:", mean_length)
print("Standard Deviation:", std_dev)
print("Minimum Text Length:", min_length)
print("Maximum Text Length:", max_length)


# total number of samples
total_samples = data.shape[0]
print("Total Samples:", total_samples, "entries")

# number of samples for each emotion
emotion_counts = data['Emotion'].value_counts()

# percentage of each emotion
emotion_percentages = data['Emotion'].value_counts(normalize=True) * 100

# Combine the counts and percentages into one DataFrame
emotion_summary = pd.DataFrame({
    'Count': emotion_counts,
    'Percentage': emotion_percentages
})

print(emotion_summary)