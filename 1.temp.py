import pandas as pd
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
#print(df)

#print(df['Name'])

#print(df.iloc[2])   # Access the third row by position
#print(df.loc[1])   # access second row by label
#print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])             # Select specific rows
unique_dates = df['Age'].unique()
high_above_102 = df[df['Age'] > 25]


df.to_csv('trading_data.csv', index=False)