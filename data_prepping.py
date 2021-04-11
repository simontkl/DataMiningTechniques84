import pandas as pd
import numpy
import seaborn as sns

df = pd.read_csv('dataset_mood_smartphone.csv')

plot = sns.pairplot(df)
print(plot)