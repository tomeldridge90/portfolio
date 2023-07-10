import pandas as pd
from interface_webscraper import create_output_df

df1 = create_output_df()

print(df1)

dataframes = [df1]

header = df1.columns

pd.DataFrame(columns=header).to_csv('/home/tome/portfolio/test_data/export.csv', index=False)

for df in dataframes:
    df.to_csv('/home/tome/portfolio/test_data/export.csv', mode='a', header=False, index=False)

