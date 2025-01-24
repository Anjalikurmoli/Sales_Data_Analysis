#Load requireed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
data = pd.read_csv('C:/Users/dhana/Downloads/Walmart_Sales.csv')

#Display the first few rows
data.head()

#Exploring the dataset
data.info()

#Checking for missing values
data.isnull().sum()

#Identifying unique values in key columns
for column in data.columns:
    print(f'{column}: {data[column].nunique()} unique values')

#handling missing values if any
data = data.dropna()

#Converting date column to date format
data['Date'] = pd.to_datetime(data['Date'], format="%d-%m-%Y", dayfirst = True)
print(data['Date'].head())

#Exploratory Data Analysis
#Sales trends over time
sales_by_date = data.groupby('Date')['Weekly_Sales'].sum().reset_index()
plt.figure(figsize=(12,6))
sns.lineplot(x='Date', y='Weekly_Sales', data=sales_by_date)
plt.title('Sales Over Time')
plt.show()

#Sales performance by Store
sales_by_store = data.groupby('Store')['Weekly_Sales'].sum().sort_values(ascending=False)
print(sales_by_store.head())
sales_by_store.plot(kind='bar', figsize=(12,6), title='Total Sales by Store')

#Impact of holidays on Sales
holiday_sales = data.groupby('Holiday_Flag')['Weekly_Sales'].mean()
holiday_sales.plot(kind='bar', figsize=(6, 4), title='Average Weekly Sales: Holiday vs Non-Holiday')

#Correlation with external factors
correlation = data[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
