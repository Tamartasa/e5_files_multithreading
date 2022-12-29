import concurrent.futures
from concurrent.futures import *
import csv
import os.path
import time


def create_files(base_prefix: str):
    if not os.path.exists(base_prefix):
        os.makedirs(base_prefix)
    executor = ThreadPoolExecutor(max_workers=8)
    futures = []

    for year, data in my_dict.items():
        file_path = os.path.join(base_prefix, f"AAPL_{year}.csv")

        future = executor.submit(write_to_file, file_path, my_data)
        futures.append(future)

    done, not_done = wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
    print(f"done: {len(done)}, not done: {len(not_done)}")


def convert_to_float(line):
    for i in range(1, len(line)):
        line[i] = float(line[i])
    return line

def calc_means(data):
    means = ['mean values', 0, 0, 0, 0, 0, 0]
    for line in data:
        for i in range(1, len(line)):
            means[i] += line[i]
    for i in range(1, len(means)):
        means[i] /= len(data)
    return means

def prepare_data(data, headers):
    means = calc_means(data)
    return [headers] + data + [means]


def write_to_file(file_path, my_data):
    with open(file_path, 'w', newline="") as fh:
        writer = csv.writer(fh)
        writer.writerows(my_data)

if __name__ == '__main__':

    start = time.time()
    with open('AAPL.csv', 'r') as f:
        reader = csv.reader(f)

        my_dict = {}
        headers = []
        # go over the file, line by line
        for line in reader:
            if not headers:
                headers = line
                continue
            convert_to_float(line)
            year = line[0][-4: ]
            if year not in my_dict:
                my_dict[year] = [line]
            my_dict[year].append(line)
        for year, data in my_dict.items():
            my_data = prepare_data(data, headers)

        create_files('AAPL_by_years')

    end = time.time()
    print(f"time: {end - start} seconds")

        # add the headers to the start of data and means to the end:

