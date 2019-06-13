import matplotlib.pyplot as plt

def main():
    """
    Parse through a tab separated text file with fields:
    Species, Observation ID, Date, Tape Time, Tape ID
    and create histogram from specific tapes to find high density 
    areas of tape to improve tape to digital conversion efficiency.
    """
    file = open(input('Enter tab separated metadata file name: '))
    all_lines = []
    for line in file:
        fields = line.split('\t')
        for i in range(len(fields)):
            single = fields[i]
            temp_single = ""
            for j in range(len(single)):
                if single[j] == ' ':
                    if j != 0 and j != len(single)-1:
                        temp_single+='_'
                elif single[j] == '\n':
                    continue
                else:
                    temp_single+=single[j]
            fields[i] = temp_single
            if fields[i] == '':
                fields.pop(i)
        all_lines.append(fields)

    occurences = species_per_tape(all_lines)
    print_tapes(occurences)
    prompt_tape(all_lines)
    start_and_end()


def uniqueFilter(all_lines):
    #for single_line in all_lines:
    return

def prompt_tape(all_lines):
    print("Search for times for specific tape? (y/n)")
    if input() == 'y':
        show_time_range(all_lines)

def species_per_tape(all_lines):
    tapes = {}
    for image in all_lines:
        if image[len(image) - 1] in tapes:
            tapes[image[len(image) - 1]] += 1
        else:
            tapes[image[len(image) - 1]] = 1
    return tapes

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
    print('Results\n', 'Tape ID'.ljust(15, ' '), 'Count'.rjust(5), sep='')
    for count in sorted(occurences, key=occurences.get):
        print(count.ljust(15, ' '), str(occurences[count]).rjust(0))

def show_time_range(all_lines):
    tapeId = input("Enter tape ID: ")
    timeStamp = {}
    for still in all_lines:
        if still[len(still)-1] == tapeId:
            t = still[3].split(':')
            seconds = int(t[2])+int(t[1])*60+int(t[0])*3600
            if seconds not in timeStamp:
                timeStamp[seconds] = 1
            else:
                timeStamp[seconds] += 1
    plt.bar(timeStamp.keys(), timeStamp.values(), color='g')
    plt.show()
    plt.savefig('histogram_'+tapeId+'.png', bbox_inches='tight')

if __name__ == '__main__':
    main()

