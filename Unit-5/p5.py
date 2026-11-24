import pandas as pd

data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Neha', 'Raj', 'Pooja', 'Karan', 'Riya', 'Jay', 'Sneha'],
    'Age': [20, 21, 19, 22, 20, 21, 20, 19, 22, 21],
    'Marks': [85, 90, 78, 95, 88, 76, 82, 91, 69, 87]
}

df = pd.DataFrame(data)

print("----- Student Data -----")
print(df)

print("\n----- First 5 Students -----")
print(df.head())

print("\n----- Last 5 Students -----")
print(df.tail())

print("\n----- Data Information -----")
df.info()

print("\n----- Statistical Summary -----")
print(df.describe())

print("\nAverage Marks:", df['Marks'].mean())

print("Highest Marks:", df['Marks'].max())

print("Lowest Marks:", df['Marks'].min())

print("\n----- Students Scoring More Than 80 -----")
print(df[df['Marks'] > 80].to_string(index=False))

print("\n----- Students Sorted by Marks -----")
print(df.sort_values(by='Marks', ascending=False).to_string(index=False))