import pandas as pd

# Create a dictionary with your data
data = {
    'age': [20, 25, 30, 4, 3, 5],
    'test_scores': [30, 35, 40, 5, 4, 6]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('data.csv', index=False)