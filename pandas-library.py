import pandas as pd

s = pd.Series([10, 20, 30, 40, 50])
df = pd.DataFrame({"Name": ["Aman", "Riya", "Kunal"],
                   "Marks": [85, 92, 78]})

print(s)                     # 0 10, 1 20, 2 30, 3 40, 4 50
print(df)                    # Data in table format

print(df["Name"])            # Aman, Riya, Kunal
print(df["Marks"])           # 85, 92, 78

print(df.iloc[0])            # First row
print(df.iloc[0, 1])         # 85
print(df.loc[1, "Name"])     # Riya

print(df.shape)              # (3, 2)
print(df.columns)            # Index(['Name', 'Marks'], dtype='object')
print(df.dtypes)             # Name: object, Marks: int64

print(df.head(2))            # First 2 rows
print(df.tail(1))            # Last row

print(df["Marks"].sum())     # 255
print(df["Marks"].mean())    # 85.0
print(df["Marks"].max())     # 92
print(df["Marks"].min())     # 78

print(df[df["Marks"] > 80])  # Rows where Marks > 80

df["Age"] = [20, 21, 19]     # Add a new column
df.drop(columns=["Age"], inplace=True)  # Remove column

print(df.sort_values("Marks"))  # Sort by Marks (ascending)
print(df["Name"].unique())      # ['Aman' 'Riya' 'Kunal']

print(df.isnull())           # Check missing values
print(df.dropna())           # Remove rows with missing values
print(df.fillna(0))           # Replace missing values with 0

print(df.groupby("Name")["Marks"].mean())  # Average Marks per Name

# Read and write CSV files
# df = pd.read_csv("data.csv")
# df.to_csv("output.csv", index=False)