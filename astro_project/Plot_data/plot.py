import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv('/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table1.csv')
df1 = df[['WEEK_NUMBER','TOTAL_ACTIVE_DEVICES']]
plt.figure(figsize=(10, 6))
palette = sns.color_palette('PuBu')
sns.barplot(data=df1, x='WEEK_NUMBER', y='TOTAL_ACTIVE_DEVICES', palette=palette, dodge=True)
plt.title('Active Device')
plt.xlabel('WEEK_NUMBER')
plt.ylabel('TOTAL_ACTIVE_DEVICES')
plt.tight_layout()
plt.legend(title='distribution', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.show()

df = pd.read_csv('/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table2.csv')
df1 = df[['WEEK_NUMBER','GENDER','TOTAL_REVENUE']]
plt.figure(figsize=(10, 6))
palette = sns.color_palette('pastel')
sns.barplot(data=df1, x='WEEK_NUMBER', y='GENDER',hue='TOTAL_REVENUE',  palette=palette, dodge=True)
plt.title('TOTAL_REVENUE')
plt.xlabel('WEEK_NUMBER')
plt.ylabel('GENDER')
plt.tight_layout()
plt.legend(title='distribution', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.show()

