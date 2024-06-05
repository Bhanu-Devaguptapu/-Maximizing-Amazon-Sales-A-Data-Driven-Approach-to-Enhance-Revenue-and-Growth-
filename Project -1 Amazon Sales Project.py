#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1STEP.First know the problem statements.
#2STEP.Collect the data from the respective sources.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import seaborn as sns
df = pd.read_csv('Amazon Sales data intern.csv')
print(df)


# In[3]:


#Find the type of the data in dataset
type(df)
df.info()
#Shape of data
df.shape 
#To find the dimensions of the data set


# In[4]:


#Find the bottom columns and rows in dataset
df.head(10)


# In[5]:


#Find the bottom columns and rows in dataset
df.tail(10)


# In[6]:


#3STEP.Clean and Prepare the data
###To find null values in the dataset
f=df.isna().sum(axis=0)
f


# In[7]:


#4STEP.Analyzing of the given dataset.
#######################
#We can find the count of unique values of dataset 
df.nunique()
#So, we can find the different unique values of the columns in the dataset.
#We can see that there are 7 different regions with 76 different countries.
#There are 12 different items are sold in 2 channels that is ONLINE and OFFLINE.
#There are 4 types of order priorities


# In[8]:


#to find the unique values in the dataset
df['Region'].unique()


# In[9]:


df['Country'].unique()


# In[10]:


df['Item Type'].unique()


# In[11]:


df['Sales Channel'].unique()


# In[12]:


df['Order Priority'].unique()
#As we can see that there are 4 order priorities like H, C, L and M.
#H means High Priority
#C means Critical Priority
#L means Low priority
#M means Medium priority


# In[13]:


#To know some statistical details regarding the dataset
df.describe() 


# In[14]:


#To find if there are any outliers in the given data
#To show the outliers in graph
plt.figure(figsize=(5, 4 * len(df.columns)))

# Iterate through each column and plot boxplot
for i, column in enumerate(df.columns):
    plt.subplot(len(df.columns), 1, i+1)
    sns.boxplot(x=df[column], color='skyblue')
    plt.title(f'Boxplot of {column}')

plt.tight_layout()
plt.show()
#By using these boxplots we can observe that there are no much outliers in the given data


# In[3]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ipywidgets import interactive

# To know the correlation and distribution between the variables
def size_widget(height=2.5, aspect=1):
    sns.pairplot(df, height=height, aspect=aspect)

interactive(size_widget, height=(1, 3.5, 0.5), aspect=(0.5, 2, 0.25))


# In[21]:


# To know the correlation and distribution between the variables
sns.pairplot(df,hue = 'Sales Channel')


# In[16]:


# Convert 'Order Date' column to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract years and months from 'Order Date' column
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

# Display the DataFrame with years and months
print(df[['Order Date', 'Year', 'Month']])


# In[17]:


#Convert 'Order Date' column to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Sort the dataset by the 'Order Date' column
df_sorted = df.sort_values(by='Order Date')

# Display the sorted DataFrame
print(df_sorted)


# In[18]:


# Convert 'Order Date' column to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract year from 'Order Date' column
df['Year'] = df['Order Date'].dt.year

# Group by 'Year' and 'Item', then sum the sales
sales_by_year_item = df.groupby(['Year', 'Item Type']).size().unstack(fill_value=0)

# Plot the sales for each item across different years
sales_by_year_item.plot(kind='bar', figsize=(12, 6))

# Set plot labels and title
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales of Items by Year')

# Show legend outside of the plot
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Show the plot
plt.show()
#In this graph we can observe the Sales of different items according to years


# In[19]:


# Group by 'Sales Channel' and 'Item Type', then sum the sales
sales_by_channel_item = df.groupby(['Sales Channel', 'Item Type']).size().unstack(fill_value=0)

# Plot the sales for each item type by sales channel
sales_by_channel_item.plot(kind='bar', figsize=(12, 6))

# Set plot labels and title
plt.xlabel('Sales Channel')
plt.ylabel('Sales')
plt.title('Sales of Item Types by Sales Channel')

# Show legend outside of the plot
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Show the plot
plt.show()
#From this graph we can observe that different item types are sold in 2 categories offline and Online


# In[20]:


# Group by 'Region' and aggregate unique values of 'Country'
countries_by_region = df.groupby('Region')['Country'].unique()

# Print countries for each region
for region, countries in countries_by_region.items():
    print(f"Region: {region}")
    print("Countries:", ", ".join(countries))
    print()
#We can observe that there are different countries belongs to different regions.


# In[21]:


# Group by 'Region' and 'Country', then sum the number of orders
orders_by_region_country = df.groupby(['Region', 'Country']).size().unstack(fill_value=0)

# Find the country with the maximum ordering history in each region
highest_ordering_country = orders_by_region_country.idxmax(axis=1)

# Plot a bar graph showing the highest shopping country with the maximum ordering history for each region
plt.figure(figsize=(10, 6))
plt.bar(highest_ordering_country.index, highest_ordering_country.values, color='pink')

# Set plot labels and title
plt.xlabel('Region')
plt.ylabel('Country with Maximum Orders')
plt.title('Highest Shopping Country with Maximum Orders in Each Region')
# Decrease the size of x-axis labels
plt.xticks(rotation=45, fontsize=8)


# In[22]:


# Create a cross-tabulation between 'Item Type' and 'Order Priority'
cross_tab = pd.crosstab(df['Item Type'], df['Order Priority'])

# Display the cross-tabulation
print(cross_tab)


# In[23]:


# Find the item type with the highest frequency for each order priority
highest_item_types = {}
for priority in df['Order Priority'].unique():
    highest_item_types[priority] = df[df['Order Priority'] == priority]['Item Type'].value_counts().idxmax()

# Plot a bar graph showing the frequency of the highest item type for each order priority
plt.figure(figsize=(10, 6))
plt.barh(range(len(highest_item_types)), list(highest_item_types.values()), color='green')

# Set the y-axis ticks and labels to be the order priorities
plt.yticks(range(len(highest_item_types)), list(highest_item_types.keys()))

# Set plot labels and title
plt.ylabel('Order Priority')
plt.xlabel('Frequency of Highest Item Type')
plt.title('Highest Item Type for Each Order Priority')

# Show the plot
plt.show()


# In[24]:


# Assuming your dataset is stored in a variable named 'df'
# Grouping by 'Item Type' and calculating total profit
item_profit = df.groupby('Item Type')['Total Profit'].sum().reset_index()

# Sorting by total profit in descending order
item_profit = item_profit.sort_values(by='Total Profit', ascending=False)

# Plotting the line graph
plt.figure(figsize=(10, 6))
plt.plot(item_profit['Item Type'], item_profit['Total Profit'], marker='o', linestyle='-')
plt.title('Total Profit by Item Type')
plt.xlabel('Item Type')
plt.ylabel('Total Profit')
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[25]:


# Grouping by 'Region', 'Country', and 'Item Type', and calculating total units sold
country_item_sales = df.groupby(['Region', 'Country', 'Item Type'])['Units Sold'].sum().reset_index()

# Sorting by total units sold in descending order within each region and country
country_item_sales_sorted = country_item_sales.groupby(['Region', 'Country']).apply(lambda x: x.sort_values(by='Units Sold', ascending=False))

# Resetting index after sorting
country_item_sales_sorted.reset_index(drop=True, inplace=True)

# Displaying the top item types in each country within each region
for (region, country), data in country_item_sales_sorted.groupby(['Region', 'Country']):
    print(f"Top item types in {country} ({region}):")
    print(data.head())  # Adjust the number in head() to show more item types if needed
    print()


# In[26]:


# Grouping by 'Region', 'Country', and calculating total units sold
region_country_sales = df.groupby(['Region', 'Country'])['Units Sold'].sum().reset_index()

# Sorting by total units sold in descending order within each region
region_country_sales_sorted = region_country_sales.sort_values(by=['Region', 'Units Sold'], ascending=[True, False])

# Plotting the data for each region
regions = region_country_sales_sorted['Region'].unique()
for region in regions:
    data = region_country_sales_sorted[region_country_sales_sorted['Region'] == region]
    plt.figure(figsize=(10, 6))
    plt.bar(data['Country'], data['Units Sold'])
    plt.title(f'Units Sold by Country in {region}')
    plt.xlabel('Country')
    plt.ylabel('Units Sold')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

