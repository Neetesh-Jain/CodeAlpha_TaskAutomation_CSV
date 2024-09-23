import pandas as pd

# Define the path to the CSV file
input_file = 'Book1.csv'  # Change this to your CSV file path
output_file = 'Book2.csv'  # Path for the cleaned CSV file

# Load the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Display the initial number of rows
print(f"Initial number of rows: {len(df)}")

# Remove rows with missing values
df_cleaned = df.dropna()

# Remove duplicate rows
df_cleaned = df_cleaned.drop_duplicates()

# Display the final number of rows
print(f"Final number of rows after cleaning: {len(df_cleaned)}")

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv(output_file, index=False)

print(f"Cleaned data has been saved to {output_file}.")
