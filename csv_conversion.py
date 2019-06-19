import csv


def query_to_csv(query_file, video_type):

    data = []
    file = open(query_file, 'r')
    for line in file:
        string = line.replace('\n', '')
        data.append(list(string.split('\t')))
    print("Read Taxa Data.")
    with open(video_type+'_data_videos.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)
    csvFile.close()
