import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# load dataset
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
df.head()
df.shape

print(f'Number of duplicated data: {df.duplicated().sum()}')
df.isnull().sum() / len(df) * 100
df.dtypes

df.describe()

#EDA
df.head()
df['Attrition'].value_counts(normalize=True)
attrition = df['Attrition'].value_counts(normalize=True)
plt.figure(figsize=(8,6))
ax = sns.barplot(x=attrition.index, y=attrition)
for p in ax.patches:
    ax.annotate(f'{p.get_height() * 100:.2f}%',
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center', va='bottom')

plt.title('Distribution of Attrition Rate')
plt.xlabel('Attrition')
plt.ylabel('Percentage')
plt.tight_layout()
plt.show()

#Employee's Demographics

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15,5))
sns.histplot(data=df, x='Age', kde=True, ax=axes[0])
axes[0].set_title('Distribution Employee by Age')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Count')
sns.countplot(data=df, x='Gender', ax=axes[1])
axes[1].set_title('Distribution Employee by Gender')
axes[1].set_xlabel('Gender')
axes[1].set_ylabel('Count')
sns.countplot(data=df, x='Department', ax=axes[2])
axes[2].set_title('Distribution Employee by Department')
axes[2].set_xlabel('Department')
axes[2].set_ylabel('Count')
plt.tight_layout()
plt.show()

