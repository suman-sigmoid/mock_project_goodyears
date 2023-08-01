#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[8]:


df = pd.read_csv('/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table1.csv')
df1 = df[['WEEK_NUMBER','TOTAL_ACTIVE_DEVICES']]


# In[9]:


plt.figure(figsize=(10, 6))
palette = sns.color_palette('PuBu')
sns.barplot(data=df1, x='WEEK_NUMBER', y='TOTAL_ACTIVE_DEVICES', palette=palette, dodge=True)
plt.title('Active Device')
plt.xlabel('WEEK_NUMBER')
plt.ylabel('TOTAL_ACTIVE_DEVICES')
plt.tight_layout()
#plt.legend(title='distribution', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.show()


# In[18]:


df = pd.read_csv('/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table2.csv')
df1 = df[['WEEK_NUMBER','GENDER','TOTAL_REVENUE']]
plt.figure(figsize=(10, 6))
palette = sns.color_palette('pastel')
sns.barplot(data=df1, x='WEEK_NUMBER', y='TOTAL_REVENUE',hue='GENDER',  palette=palette, dodge=True)
plt.title('TOTAL_REVENUE')
plt.xlabel('WEEK_NUMBER')
plt.ylabel('TOTAL_REVENUE')
plt.tight_layout()
plt.legend(title='distribution', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.show()


# In[22]:


df = pd.read_csv('/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table4.csv')
df1 = df[['WEEK_NUMBER','MOBILE_TYPE','TOTAL_REVENUE']]
plt.figure(figsize=(10, 6))
palette = sns.color_palette('pastel')
sns.barplot(data=df1, x='MOBILE_TYPE', y='WEEK_NUMBER',hue='TOTAL_REVENUE',  palette=palette, dodge=True)
plt.title('TOTAL_REVENUE')
plt.xlabel('MOBILE_TYPE')
plt.ylabel('WEEK_NUMBER')
plt.tight_layout()
plt.legend(title='distribution', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.show()


# In[95]:


df = pd.read_csv('/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table6.csv')
df1 = df[['WEEK_NUMBER','OS_NAME','TOTAL_REVENUE']]
grouped_df = df1.groupby(['WEEK_NUMBER', 'OS_NAME'])['TOTAL_REVENUE'].sum().reset_index()
print(grouped_df)
unique_name = df1['OS_NAME'].unique()
palette = sns.color_palette('flare')


for name in unique_name:
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df1[df1['OS_NAME'] == name], x='WEEK_NUMBER', y='TOTAL_REVENUE',palette=palette, ci=None)
    plt.title(f'Bar Chart for {name}')
    plt.xlabel('Week Number')
    plt.ylabel('TOTAL_REVENUE')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# In[92]:


df = pd.read_csv('/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table7.csv')
df1 = df[['WEEK_NUMBER','OS_VENDOR','TOTAL_REVENUE']]

grouped_df = df1.groupby(['WEEK_NUMBER', 'OS_VENDOR'])['TOTAL_REVENUE'].sum().reset_index()
print(grouped_df)
unique_name = df1['OS_VENDOR'].unique()
palette = sns.color_palette('hot')


for name in unique_name:
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df1[df1['OS_VENDOR'] == name], x='WEEK_NUMBER', y='TOTAL_REVENUE',palette=palette, ci=None)
    plt.title(f'Bar Chart for {name}')
    plt.xlabel('Week Number')
    plt.ylabel('TOTAL_REVENUE')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# In[89]:


df = pd.read_csv('/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table10.csv')
df1= df[['WEEK_NUMBER','OS_NAME','HIGHEST_REVENUE_BY_OSNAME']]
grouped_df = df1.groupby(['WEEK_NUMBER', 'OS_NAME'])['HIGHEST_REVENUE_BY_OSNAME'].sum().reset_index()
print(grouped_df)
unique_name = df1['OS_NAME'].unique()
palette = sns.color_palette('pastel')


for name in unique_name:
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df1[df1['OS_NAME'] == name], x='WEEK_NUMBER', y='HIGHEST_REVENUE_BY_OSNAME',palette=palette, ci=None)
    plt.title(f'Bar Chart for {name}')
    plt.xlabel('Week Number')
    plt.ylabel('HIGHEST_REVENUE_BY_OSNAME')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# In[87]:


df = pd.read_csv('/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table11.csv')
df1= df[['WEEK_NUMBER','OS_NAME','LOWEST_REVENUE_BY_OSNAME']]
grouped_df = df1.groupby(['WEEK_NUMBER', 'OS_NAME'])['LOWEST_REVENUE_BY_OSNAME'].sum().reset_index()
print(grouped_df)
unique_name = df1['OS_NAME'].unique()
palette = sns.color_palette('pastel')


for name in unique_name:
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df1[df1['OS_NAME'] == name], x='WEEK_NUMBER', y='LOWEST_REVENUE_BY_OSNAME',palette=palette, ci=None)
    plt.title(f'Bar Chart for {name}')
    plt.xlabel('Week Number')
    plt.ylabel('LOWEST_REVENUE_BY_OSNAME')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# In[78]:


df = pd.read_csv("/Users/suman_choudhary1/Desktop/astro_project/Plot_data/part2_table.csv")
df1= df[['WEEK_NUMBER','OS_NAME','TOTAL_CUSTOMER_DISTRIBUTION_OS_NAME']]
df2 = df[['WEEK_NUMBER','BRAND_NAME','TOTAL_CUSTOMER_DISTRIBUTION_BRAND_NAME']]
df3 = df[['WEEK_NUMBER','MOBILE_TYPE','TOTAL_CUSTOMER_DISTRIBUTION_MOBILE_TYPE']]



# In[77]:


df1= df[['WEEK_NUMBER','OS_NAME','TOTAL_CUSTOMER_DISTRIBUTION_OS_NAME']]
grouped_df = df1.groupby(['WEEK_NUMBER', 'OS_NAME'])['TOTAL_CUSTOMER_DISTRIBUTION_OS_NAME'].sum().reset_index()
print(grouped_df)
unique_name = df1['OS_NAME'].unique()
light_color = '#ADD8E6' 

for name in unique_name:
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df1[df1['OS_NAME'] == name], x='WEEK_NUMBER', y='TOTAL_CUSTOMER_DISTRIBUTION_OS_NAME', color=light_color, ci=None)
    plt.title(f'Bar Chart for {name}')
    plt.xlabel('Week Number')
    plt.ylabel('TOTAL_CUSTOMER_DISTRIBUTION_OS_NAME')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# In[86]:


grouped_df = df2.groupby(['WEEK_NUMBER', 'BRAND_NAME'])['TOTAL_CUSTOMER_DISTRIBUTION_BRAND_NAME'].sum().reset_index()
print(grouped_df)
unique_name = df2['BRAND_NAME'].unique()
light_color = '#ADD8E6' 

for name in unique_name:
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df2[df2['BRAND_NAME'] == name], x='WEEK_NUMBER', y='TOTAL_CUSTOMER_DISTRIBUTION_BRAND_NAME', color=light_color, ci=None)
    plt.title(f'Bar Chart for {name}')
    plt.xlabel('Week Number')
    plt.ylabel('TOTAL_CUSTOMER_DISTRIBUTION_BRAND_NAME')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# In[39]:


grouped_df = df3.groupby(['WEEK_NUMBER', 'MOBILE_TYPE'])['TOTAL_CUSTOMER_DISTRIBUTION_MOBILE_TYPE'].sum().reset_index()

# Print the resulting DataFrame.
print(grouped_df)


# In[54]:



plt.figure(figsize=(10, 6))
palette = sns.color_palette('pastel')

sns.barplot(data=grouped_df, x='WEEK_NUMBER', y='TOTAL_CUSTOMER_DISTRIBUTION_MOBILE_TYPE', hue='MOBILE_TYPE', palette=palette)
plt.title('Distribution')
plt.xlabel('WEEK_NUMBER')
plt.ylabel('TOTAL_CUSTOMER_DISTRIBUTION_MOBILE_TYPE')
plt.tight_layout()
plt.legend(title='Distribution', bbox_to_anchor=(1.02, 1), loc='upper left')

plt.show()


# In[56]:


dff = pd.read_csv("/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table3.csv")
plt.figure(figsize=(10, 6))
for age in dff['CUSTOMER_AGE'].unique():
    age_data = dff[dff['CUSTOMER_AGE'] == age]
    plt.bar(age_data['WEEK_NUMBER'], age_data['TOTAL_REVENUE'], label=f'Age {age}')

plt.title('Total Revenue by Week Number')
plt.xlabel('Week Number')
plt.ylabel('Total Revenue')
plt.legend(title='Customer Age',bbox_to_anchor=(1.02, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[68]:


df = pd.read_csv('/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table12.csv')
df1 = df[['BRAND_NAME','BRAND_CUSTOMER']]
plt.figure(figsize=(10, 6))
palette = sns.color_palette('hot')
sns.barplot(data=df1, x='BRAND_NAME', y='BRAND_CUSTOMER',  palette=palette, dodge=True)
plt.title('BRAND_CHOOSEN_BETWEEN(20-30)')
plt.xlabel('BRAND_NAME')
plt.ylabel('BRAND_CUSTOMER')
plt.tight_layout()
#plt.legend(title='distribution', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[67]:


df = pd.read_csv('/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table13.csv')
df1 = df[['OS_NAME','OS_CUSTOMER']]
plt.figure(figsize=(10, 6))
palette = sns.color_palette('hot_r')
sns.barplot(data=df1, x='OS_NAME', y='OS_CUSTOMER',  palette=palette, dodge=True)
plt.title('OS_CHOOSEN_BETWEEN(20-30)')
plt.xlabel('OS_NAME')
plt.ylabel('OS_CUSTOMER')
plt.tight_layout()
#plt.legend(title='distribution', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[70]:


df4 = pd.read_csv('/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table5.csv')
unique_brands = df4['BRAND_NAME'].unique()
for brand in unique_brands:
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df4[df4['BRAND_NAME'] == brand], x='WEEK_NUMBER', y='TOTAL_REVENUE', palette='husl', ci=None)
    plt.title(f'Bar Chart for {brand}')
    plt.xlabel('Week Number')
    plt.ylabel('Total Revenue')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# In[72]:


df5 = pd.read_csv('/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table8.csv')
unique_brands = df5['BRAND_NAME'].unique()
for brand in unique_brands:
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df5[df5['BRAND_NAME'] == brand], x='WEEK_NUMBER', y='HIGHEST_REVENUE_BY_BRANDNAME', palette='husl', ci=None)
    plt.title(f'Bar Chart for {brand}')
    plt.xlabel('Week Number')
    plt.ylabel('HIGHEST_REVENUE_BY_BRANDNAME')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# In[73]:


df6 = pd.read_csv('/Users/suman_choudhary1/Desktop/astro_project/Plot_data/table9.csv')
unique_brands = df6['BRAND_NAME'].unique()
for brand in unique_brands:
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df6[df6['BRAND_NAME'] == brand], x='WEEK_NUMBER', y='LOWEST_REVENUE_BY_BRANDNAME', palette='husl', ci=None)
    plt.title(f'Bar Chart for {brand}')
    plt.xlabel('Week Number')
    plt.ylabel('LOWEST_REVENUE_BY_BRANDNAME')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# In[ ]:




