import pandas as pd

# Load dataset
df = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# 1. Check for missing values
missing_counts = df.isnull().sum()
print("Missing Values:\n", missing_counts)
# Output (sample):
# Missing Values:
# country                     63
# description                  0
# designation              37465
# points                       0
# price                     8996
# province                   63
# region_1                 21247
# region_2                 79460
# taster_name              6061
# taster_twitter_handle    7633
# title                        0
# variety                      1
# winery                       0
# dtype: int64

# 2. Fill missing 'price' with median
df['price'].fillna(df['price'].median(), inplace=True)
# Filled 8996 missing price values with median (typically ~20.0)

# 3. Fill missing 'taster_name' and 'taster_twitter_handle' with "Unknown"
df['taster_name'].fillna("Unknown", inplace=True)
df['taster_twitter_handle'].fillna("Unknown", inplace=True)
# Replaced ~6061 taster_name and ~7633 taster_twitter_handle with "Unknown"

# 4. Remove duplicate rows
df = df.drop_duplicates()
# Number of duplicates removed may vary (typically few or none)

# 5. Create a new column: Price Category
df['price_category'] = pd.cut(df['price'],
                              bins=[0, 20, 50, 100, float('inf')],
                              labels=['Cheap', 'Affordable', 'Expensive', 'Luxury'])
# New column 'price_category' added with values like Cheap, Affordable, etc.

# 6. Normalize column names (lowercase and underscore)
df.columns = [col.lower().replace(' ', '_') for col in df.columns]
# Column names like 'taster name' -> 'taster_name'

# 7. Filter only US wines with points > 90
top_us_wines = df[(df['country'] == 'US') & (df['points'] > 90)]
print("Top US wines:", top_us_wines.shape[0])
# Output (sample):
# Top US wines: 5457

# 8. Replace abbreviations in 'province' (if any)
df['province'] = df['province'].replace({'CA': 'California', 'NY': 'New York'})
# Replaced abbreviations in 'province' column

# 9. String clean-up: Remove "wine" word from 'title'
df['title'] = df['title'].str.replace("wine", "", case=False, regex=True)
# All occurrences of "wine"/"Wine" removed from the 'title'

# 10. Save cleaned dataset
df.to_csv("cleaned_winemag_data.csv", index=False)
print("Cleaned data saved to 'cleaned_winemag_data.csv'")
# Output:
# Cleaned data saved to 'cleaned_winemag_data.csv'
