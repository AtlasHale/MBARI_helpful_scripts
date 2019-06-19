import csv
import re


def analyze_csv(file_name):

    reader = csv.reader(open(file_name), delimiter=",")
    next(reader)  # Skips header
    sorted_list = sorted(reader, key=lambda row: row[4], reverse=False)
    sorted_list = sorted(sorted_list, key=lambda row: row[1], reverse=False)

    video_species = {}
    for data in sorted_list:
        if data[4] in video_species:
            if data[0] in video_species[data[4]]:
                video_species[data[4]][data[0]] += 1
            else:
                video_species[data[4]][data[0]] = 1
        else:
            video_species[data[4]] = {}
            video_species[data[4]][data[0]] = 1

    return video_species


def analysis_to_text_overview(data, video_type):

    with open(video_type + '_all_taxa_analyzed_overview.txt', 'w') as file:
        viewed_taxa = set()
        file.write('Species:\n')
        for video in data:
            for taxa in data[video]:
                if re.search('[A-Z]', taxa):
                    viewed_taxa.add(taxa)
        viewed_taxa = sorted(viewed_taxa)
        for taxa in viewed_taxa:
            file.write('\t\t' + taxa + '\n')
    file.close()


def analysis_to_text_individual_video(data, video_type):

    with open(video_type + '_all_taxa_analyzed_individual_video.txt', 'w') as file:
        viewed_taxa = set()
        for video in data:
            file.write('VideoCode: ' + video + '\n' + 'Species:\n')
            for taxa in data[video]:
                if re.search('[A-Z]', taxa):
                    viewed_taxa.add(taxa)
            viewed_taxa = sorted(viewed_taxa)
            for taxa in viewed_taxa:
                file.write('\t\t' + taxa + '\n')
            file.write('\n')
            viewed_taxa = set()
    file.close()


def combine_analysis_overview():

    file1 = input('Enter first overview txt file: ')
    file2 = input('Enter second overview txt file: ')
    files = [file1, file2]
    with open('all_data_videos.txt', 'w') as outfile:
        for file in files:
            with open(file) as infile:
                for line in infile:
                    line = line.replace('\t', '')
                    line = line.strip(' ')
                    outfile.write(line)
    outfile.close()


def remove_duplicates():

    lines_seen = set()  # holds lines already seen
    filename = input('Enter filename: ')
    for line in open(filename, "r"):
        lines_seen.add(line)
    lines_seen = sorted(lines_seen)
    with open('all_species.txt', 'w') as outfile:
        for line in lines_seen:
            outfile.write(line)
    outfile.close()
