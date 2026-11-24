import pandas as pd

df = pd.read_csv("student_data.csv")

print("\n----- Student Data from CSV File -----")
print(df.to_string(index=False))

print("\n----- First 5 Records -----")
print(df.head())

print("\n----- Last 5 Records -----")
print(df.tail())

print("\n----- DataFrame Information -----")
df.info()

print("\n----- Statistical Summary -----")
print(df.describe())

print("\nTotal Students:", len(df))

print("\n----- Average Marks -----")
print("Math Average:", df['Math'].mean())
print("Science Average:", df['Science'].mean())
print("English Average:", df['English'].mean())

print("\nHighest Total Marks:", df['Total'].max())
print("Lowest Total Marks:", df['Total'].min())

print("\n----- Passed Students -----")
print(df[df['Pass'] == 'Yes'].to_string(index=False))

print("\n----- Failed Students -----")
print(df[df['Pass'] == 'No'].to_string(index=False))

print("\nTotal Passed Students:", (df['Pass'] == 'Yes').sum())
print("Total Failed Students:", (df['Pass'] == 'No').sum())

pass_percentage = (df['Pass'].eq('Yes').sum() / len(df)) * 100
print("Pass Percentage:", pass_percentage, "%")

print("\n----- Students Sorted by Total Marks -----")
print(df.sort_values(by='Total', ascending=False).to_string(index=False))