import time
tic = time.perf_counter()
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt, mpld3
from pandas import DataFrame
#----------------------------------------------------------------------------------------------------------------------#
#Load the data into a DF
with open(r"C:/Users/Pathtoyourdata", 'r', encoding='utf8', errors='ignore') as read_file:
    json_reloaded = json.load(read_file)
print(len(json_reloaded))
complete_data = pd.DataFrame(json_reloaded)
print(complete_data.head()) #head

def artists():
    df_top_freq = complete_data.groupby(['artistName'])['artistName'].agg(
        {"artist_count": len}).sort_values("artist_count", ascending=False)

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df_top_freq)
        df_top_freq.to_csv('top_artists.csv')

def songs():
    df_top_songs = complete_data.groupby(["trackName"])["trackName"].agg(
        {"song_count": len}).sort_values("song_count", ascending=False)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df_top_songs)
        df_top_songs.to_csv('top_songs.csv')
songs()
artists()



toc = time.perf_counter()
print(f" {toc - tic:0.4f} seconds")