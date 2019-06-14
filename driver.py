import pprint
import csv_conversion as cc
import find_relatable_videos as frl

query_filename = 'RareTaxaVideos.txt'
csv_filename = 'genus_data_videos.csv'

cc.query_to_csv(query_filename)
data = frl.analyze_csv(csv_filename)

pprint.pprint(data)

frl.analyze_best_videos(data)