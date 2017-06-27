# -*- coding: utf-8 -*-

import argparse
import csv
import pathlib
import json


def read_csv(path):
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, skipinitialspace=True, delimiter=',')

        data = []
        for row in reader:
            if row['Mid'].startswith('PTY'):
                row['PTY'] = row['Mid'].split('PTY ')[-1]
                row['Mid'] = None
            if row['Mid'] == 'NMN':
                row['Mid'] = None
            data.append(row)

        return data


def write_data(data, dest=None, typ=None):
    if typ is None:
        typ = 'json'
    if dest.suffix.endswith('json'):
        typ = 'json'

    if typ == 'json':
        data = json.dumps(data, ensure_ascii=False, indent=4)

    if dest:
        with open(dest, 'w') as f:
            f.write(data)
            f.write('\n')
    else:
        print(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help='input csv')
    parser.add_argument('-w', '--write', type=str, help='output file')

    args = parser.parse_args()
    if args.input:
        data = read_csv(args.input)
        dest = pathlib.Path(args.write)
        write_data(data, dest)
