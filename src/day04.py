import datetime
import time

import pandas as pd


def load_data():
    with open('./input/day04.txt', 'r') as f:
        table = str.maketrans(dict.fromkeys('[-:]#', ' '))
        data = [line.translate(table).split() for line in f.read().strip().split('\n')]
        data = [(datetime.datetime(*list(map(int, line[0:5]))), ' '.join(line[5:])) for line in data]
        return sorted(data)


def data_frame(data):
    columns = ['Date', 'ID'] + [f'{min:02d}' for min in list(range(0, 60))]
    df = pd.DataFrame(columns=columns)
    start = ''
    end = ''
    for record in data:
        date = f'{record[0].year}-{record[0].month}-{record[0].day}'
        if 'Guard' in record[1]:
            id = int(record[1].split()[1])
        if record[1] == 'falls asleep':
            start = record[0].minute
        if record[1] == 'wakes up':
            end = record[0].minute
        if start != '' and end != '':
            df = df.append(pd.DataFrame([[date, id] + [1 if num in list(range(start, end)) else 0 for num in list(range(0, 60))]], columns=columns))
            start = ''
            end = ''
    df[columns[2:]] = df[columns[2:]].astype('int')
    return df.reset_index(drop=True)


def part_one(df):
    id = int(df.groupby('ID').sum().sum(axis=1).idxmax())
    min = int(df[df['ID'] == id].groupby('ID').sum().idxmax(axis=1).values)
    return id * min


def part_two(df):
    min = int(df.groupby('ID').sum().max().idxmax())
    id = int(df.groupby('ID').sum()[str(min)].idxmax())
    return id * min


if __name__ == '__main__':
    data = load_data()
    df = data_frame(data)
    print(part_one(df))
    print(part_two(df))
