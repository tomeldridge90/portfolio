import pandas as pd
from web_scrapers.interface_webscraper import create_output_df

output_path = '/home/tome/portfolio/test_data/export.csv'

df1 = create_output_df()
dataframes = [df1]

def combine_dataframes(dataframes):
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df

def append_dataframes_to_csv(dataframes, output_path):
    header = dataframes[0].columns
    pd.DataFrame(columns=header).to_csv(output_path, index=False)

    for df in dataframes:
        df.to_csv(output_path, mode='a', header=False, index=False)

def tiles_export_df():
    return combine_dataframes(dataframes)

#append_dataframes_to_csv(dataframes, output_path)

