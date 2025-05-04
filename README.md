# task11
# 🍷 Wine Reviews - Data Cleaning Practice

This project is a practical exercise based on **Chapter 7: Data Cleaning and Preparation** from *Wes McKinney's "Python for Data Analysis (2022)"*. It demonstrates various essential data cleaning techniques using the `pandas` library.

## 📊 Dataset
**Source:** [Wine Reviews Dataset (Kaggle)](https://www.kaggle.com/zynicide/wine-reviews)  
**File used:** `winemag-data-130k-v2.csv`

## 🧹 Cleaning & Preparation Steps

The cleaning script performs the following:

1. **Handling Missing Values**
   - Filled missing `price` values with the median.
   - Replaced missing `taster_name` and `taster_twitter_handle` with `"Unknown"`.

2. **Removing Duplicates**
   - Dropped any duplicate rows.

3. **Creating New Columns**
   - Added a new column `price_category` to classify wine prices into bins (`Cheap`, `Affordable`, etc.).

4. **Normalizing Column Names**
   - Converted all column names to lowercase with underscores.

5. **Filtering Rows**
   - Extracted only US wines with a score (`points`) above 90.

6. **Replacing Values**
   - Replaced abbreviations in the `province` column (e.g., `CA` → `California`).

7. **String Cleaning**
   - Removed the word `"wine"` from the `title` column.

8. **Saving Cleaned Data**
   - Final cleaned dataset is saved as `cleaned_winemag_data.csv`.

## 💻 How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/wine-data-cleaning.git
cd wine-data-cleaning

# Install requirements (if needed)
pip install pandas

# Run the script
python wine_cleaning_practice.py
