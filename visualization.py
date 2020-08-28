import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='order')

print(presidents_df.head())

#Single Indexing
presidents_df.loc[5]

#Multiple Indexing
presidents_df.loc['John Tyler':'Abraham Lincoln']
presidents_df.iloc[5:15] #John Quincy Adams till James Buchanan

#shape
presidents_df['height'].shape

#Min Max Values for all Attributes (columns)
presidents_df.min()
presidents_df.max()

#mean and median
presidents_df.mean()
presidents_df.median()

#Quartiles for Age
age_quartiles = presidents_df['age'].quantile([0.25,0.5,0.75,1])
age_quartiles = np.array(age_quartiles)
print(age_quartiles)

#Plot Age
fig = plt.figure()
fig.set_size_inches(18.5, 10.5, forward=True)
ax1 = fig.add_subplot(111)
ax1.scatter(presidents_df['name'], presidents_df['age'])
plt.xticks(rotation=90)
ax1.tick_params(axis='x', length=15, labelsize=14)
plt.show()
