import csv

with open('AAPL.csv', 'r') as f:
    reader = csv.reader(f)
    # go over the file, line by line

    my_dict = {}
    headers = []
    # for each line:
    # convert all values but the date to floats:
    for line in reader:
        if not headers:
            headers = line
            continue
        for i in range(1, len(line)):
            line[i] = float(line[i])
    # look at the year XXXX
    # if the year is not already in d - add it as a key, and the [line] as a value
        year = line[0][-4: ]
        if year not in my_dict:
            my_dict[year] = [line]
        my_dict[year].append(line)

    # go over the keys (years) in d
    # for each year:
    # add the headers to the start of data and means to the end:
    # go over the data (value) line by line XXXX
    # add the line into the file, sum up ['mean values', Low,	Open,	Volume,	High,	Close,	Adjusted Close] XXX

    for year, data in my_dict.items():
        means = ['mean values', 0, 0, 0, 0, 0, 0]
        for line in data:
            for i in range(1, len(line)):
                means[i] += line[i]

    # divide all the mean values by len(data), and add the mean line to the end of data
    for i in range(1, len(means)):
        means[i] /= len(data)

for year, data in my_dict.items():
    data = [headers] + data + [means]
    # write data into a new file
    with open(f'AAPL_by_years\\AAPL_{year}.csv', 'w', newline="") as fh:
        writer = csv.writer(fh)
        writer.writerows(data)
