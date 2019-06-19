import csv_conversion as cc
import data_analysis as da

query_filename = input('Enter query filename: ')
csv_filename = input('Enter csv filename: ')
video_type = input('What type of taxa? (ex. Rare, Common, All...) : ')

cc.query_to_csv(query_filename, video_type)
data = da.analyze_csv(csv_filename)
da.analysis_to_text_overview(data, video_type)
da.combine_analysis_overview()
da.remove_duplicates()