import matplotlib.pyplot as plt
import os
import csv


def main():
    """
    Parse through a tab separated text file with fields:
    Species, Observation ID, Date, Tape Time, Tape ID
    and create histogram from specific tapes to find high density 
    areas of tape to improve tape to digital conversion efficiency.
    """
    file = open('updated')
    all_lines = []
    for line in file:
        fields = line.split('\t')
        # remove trailing newlines, spaces replaced with _
        for i in range(len(fields)):
            fields[i] = fields[i].strip(' \n\t').replace(' ','_')
        all_lines.append(fields)
    for x in all_lines:
        print(x)
    # query_to_csv()
    # occurences = species_per_tape(all_lines)
    # print_tapes(occurences)
    # species_split_histogram(all_lines, input("Video ID: "))
    # specific_species(all_lines)
    # prompt_tape(all_lines)
    # start_and_end()
    # print_all(all_lines)


def prompt_tape(all_lines):
    print("Search for times for specific tape? (y/n)")
    if input() == 'y':
        show_time_range(all_lines)
    else:
        exit(0)


def species_per_tape(all_lines):
    tapes = {}
    for image in all_lines:
        if image[len(image) - 1] in tapes:
            tapes[image[len(image) - 1]] += 1
        else:
            tapes[image[len(image) - 1]] = 1
    return tapes


def specific_species(all_lines):
    choice = input("Enter species: ")
    tapes = {}
    for image in all_lines:
        if image[0] == choice:
            if image[len(image) - 1] not in tapes:
                tapes[image[len(image) - 1]] = 1
            else:
                tapes[image[len(image) - 1]] += 1
    print(tapes)
    print('Results for '+choice)
    for count in sorted(tapes, key=tapes.get):
        print(str(count).ljust(15, ' '), str(tapes[count]).rjust(0))


def start_and_end():
    start = int(input("Enter start seconds: "))
    end = int(input("Enter end seconds: "))
    s = str(start//3600)+':'
    start %=3600
    s += str(start//60)+':'
    start %=60
    s += str(start)+':00'
    e = str(end//3600)+':'
    end %=3600
    e += str(end//60)+':'
    end %=60
    e += str(end)+':00'
    print('Start: '+s, 'End: '+e, sep='\n')


def print_tapes(occurences):
    print('Tape ID'.ljust(15, ' '), 'Count'.rjust(5), sep='')
    for count in sorted(occurences, key=occurences.get):
        print(str(count).ljust(15, ' '), str(occurences[count]).rjust(0))


def show_time_range(all_lines):
    """Generate histogram to see species density throughout """
    tape_id = input("Enter tape ID: ")
    timeStamp = {}
    for still in all_lines:
        if still[len(still)-1] == tape_id:
            t = still[3].split(':')
            seconds = int(t[2])+int(t[1])*60+int(t[0])*3600
            if seconds not in timeStamp:
                timeStamp[seconds] = 1
            else:
                timeStamp[seconds] += 1
    plt.bar(timeStamp.keys(), timeStamp.values(), color='g')
    plt.show()
    plt.savefig('histogram_'+tape_id+'.png', bbox_inches='tight')


def species_split_histogram(all_lines, video_id):
    video = {}
    timestamp = {}
    for selection in all_lines:
        if selection[len(selection)-1] == video_id:
            if selection[0] not in video:
                t = selection[3].split(':')
                seconds = int(t[2]) + int(t[1]) * 60 + int(t[0]) * 3600
                timestamp[seconds] = selection[3]
                video[selection[0]] = [seconds]
            else:
                t = selection[3].split(':')
                seconds = int(t[2]) + int(t[1]) * 60 + int(t[0]) * 3600
                timestamp[seconds] = selection[3]
                video[selection[0]].append(seconds)
    all_species = []
    colors = ['#E69F00', '#0000FF', '#D55E00', '#F0E442', '#000000', ]
    c = []
    i = 0
    for key in video.keys():
        subset_timestamps = video[key]
        all_species.append(subset_timestamps)
        c.append(colors[i])
        i += 1
        print(key)
        for ts in subset_timestamps:
            print(timestamp[ts])
        print()
    plt.hist(all_species, color=c, label=video.keys())

    plt.legend(prop={'size': 12}, title=video_id)
    plt.title(video_id)
    plt.xlabel('Time')
    plt.ylabel('Density')
    if 'species_density_'+video_id+'.png' in os.listdir():
        os.remove('species_density_'+video_id+'.png')
    plt.savefig('species_density_'+video_id+'.png', bbox_inches='tight')
    plt.show()


def print_all(all_lines):
    seen = set()
    for x in all_lines:
        if x[len(x)-1] not in seen:
            seen.add(x[len(x)-1])
            curr = x[len(x)-1]
            print(x[len(x)-1])
            for y in all_lines:
                if y[len(y)-1] == curr:
                    print(
                        str(y[0]).ljust(40, ' '),
                        str(y[len(y)-2]).ljust(25, ' '),
                        str(y[len(y)-3]))
            print()



def query_to_csv():
    data = []

    file = open('updated', 'r')
    for line in file:
        string = line.replace('\n', '')
        data.append(list(string.split('\t')))
    print("Read Taxa Data.")

    with open('genus_data_videos.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)
    csvFile.close()

if __name__ == '__main__':
    main()

