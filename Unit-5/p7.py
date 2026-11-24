import pandas as pd
import numpy as np

data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Neha', 'Raj',
             'Pooja', 'Karan', 'Riya', 'Jay', 'Sneha'],
    'Age': [20, 21, np.nan, 22, 20, 21, np.nan, 19, 22, 21],
    'Marks': [85, np.nan, 78, 95, 88, np.nan, 82, 91, 69, 87]
}

df = pd.DataFrame(data)

print("----- Original DataFrame -----")
print(df)

print("\n----- Missing Values -----")
print(df.isnull().sum())

# Remove rows containing missing values
df_drop = df.dropna()

print("\n----- DataFrame After dropna() -----")
print(df_drop)

# Fill missing values with 0
df_fill = df.fillna(0)

print("\n----- DataFrame After fillna() -----")
print(df_fill)

# Fill missing Age with average Age
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("\n----- DataFrame After Filling Average Age -----")
print(df)
