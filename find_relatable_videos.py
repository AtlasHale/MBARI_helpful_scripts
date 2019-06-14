import csv


def analyze_csv(file_name):

    reader = csv.reader(open(file_name), delimiter=",")
    next(reader) # Skips header
    sorted_list = sorted(reader, key=lambda row: row[4], reverse=False)
    sorted_list = sorted(sorted_list, key=lambda row: row[1], reverse=False)

    video_species = {}
    for data in sorted_list:
        if data[4] in video_species:
            if data[0] in video_species[data[4]]:
                video_species[data[4]][data[0]]+=1
            else:
                video_species[data[4]][data[0]]=1
        else:
            video_species[data[4]] = {}
            video_species[data[4]][data[0]] = 1

    return video_species


def analyze_best_videos(data):
    chart_list = [['VideoCode', 'Unique Species', 'Peniagone', 'Oneirophanta Mutabilis Complex',
                   'Cystechinus Loveni', 'Fungiacyathus Marenzelleri', 'Echinocrepis']]
    for video_code in data:
        video_list = []
        uniques = 0
        p = 0
        o = 0
        cs = 0
        fm = 0
        e = 0
        for taxa in data[video_code]:
            if taxa == 'Peniagone sp. 1 ':
                uniques += 1
                p = data[video_code][taxa]
            if taxa == 'Oneirophanta mutabilis complex ':
                uniques += 1
                o = data[video_code][taxa]
            elif taxa == 'Cystechinus loveni ':
                uniques += 1
                cs = data[video_code][taxa]
            elif taxa == 'Fungiacyathus (Bathyactis) marenzelleri ':
                uniques += 1
                fm = data[video_code][taxa]
            elif taxa == 'Echinocrepis ':
                uniques += 1
                e = data[video_code][taxa]

        video_list.extend([video_code, uniques, p, o, cs, fm, e])
        chart_list.append(video_list)

    with open('genus_data_brokendown.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(chart_list)
    csvFile.close()



