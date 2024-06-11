import pandas as pd

data = pd.read_csv('C:/Users/tiger/Desktop/tez/multimedia/paper/paper m/data/Emotion_classify_Data.csv')

emotions = data['Emotion'].unique()

subsets = {emotion: data[data['Emotion'] == emotion] for emotion in emotions}

joy_data = subsets['joy']

for emotion, subset in subsets.items():
    print(f"Number of entries for {emotion}: {len(subset)}")

for emotion, subset in subsets.items():
    subset.to_csv(f'{emotion}_subset.csv', index=False)



