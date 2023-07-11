import sys
import os

print(os.getcwd())

from web_scrapers.tiles_export import tiles_export_df


class tiles_pipeline:
    def __init__(self):
        self.bucket_name = 'customer_showroom'
        self.data = tiles_export_df()
