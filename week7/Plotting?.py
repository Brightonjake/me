import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = gpd.read_file('week7/formatted_SA2.geojson')

print(type(df))