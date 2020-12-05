import csv
from collections import namedtuple
from pathlib import Path
from datetime import datetime


# Goal 1
# Your first task is to create iterators for each of the four files that contained cleaned up data, of the correct type
# (e.g. string, int, date, etc), and represented by a named tuple.
# For now these four iterators are just separate, independent iterators.

def read_csv(file_name):
    """
    A generator that reads one line at a time from the csv file
    :param file_name:
    :return: generator
    """
    with open(file_name, 'r') as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        yield from rows


def personal_info():
    """
    Generator to read the personal_info csv file
    :return:
    """
    data = read_csv(Path(__file__).parent.joinpath('data/personal_info.csv'))
    field_names = next(data)
    field_types = [str, str, str, str, str]
    Personal_Info = namedtuple('Info', field_names)

    for record in data:
        record = [t(x) for t, x in zip(field_types, record)]
        yield Personal_Info(*record)


def vehicles():
    """
    Generator to read the vehicles.csv file
    :return:
    """
    data = read_csv(Path(__file__).parent.joinpath('data/vehicles.csv'))
    field_names = next(data)
    field_types = [str, str, str, int]
    Vehicles = namedtuple('Vehicles', field_names)

    for record in data:
        record = [t(x) for t, x in zip(field_types, record)]
        yield Vehicles(*record)


def employment():
    """
    Generator to read the employment.csv file
    :return:
    """
    data = read_csv(Path(__file__).parent.joinpath('data/employment.csv'))
    field_names = next(data)
    field_types = [str, str, str, str]
    Employment = namedtuple('Employment', field_names)

    for record in data:
        record = [t(x) for t, x in zip(field_types, record)]
        yield Employment(*record)


def update_status():
    """
    Generator to read the update_status.csv file
    :return:
    """
    data = read_csv(Path(__file__).parent.joinpath('data/update_status.csv'))
    field_names = next(data)

    def date_formatter(x):
        return datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ')

    field_types = [str, date_formatter, date_formatter]
    Update_Status = namedtuple('Update_Status', field_names)

    for record in data:
        record = [t(x) for t, x in zip(field_types, record)]
        yield Update_Status(*record)


# noinspection PyProtectedMember,PyUnresolvedReferences
def full_record():
    """
    Goal 2
    Create a single iterable that combines all the columns from all the iterators.
    The iterable should yield named tuples containing all the columns. Make sure that the SSN's across the files match!
    All the files are guaranteed to be in SSN sort order, and every SSN is unique, and every SSN appears in every file.
    Make sure the SSN is not repeated 4 times - one time per row is enough!

    Generator to read the data from all the csv files, and combine into a single record
    :return:
    """
    data1 = employment()
    data2 = personal_info()
    data3 = update_status()
    data4 = vehicles()

    for item in zip(data1, data2, data3, data4):
        assert (item[0].ssn == item[1].ssn == item[2].ssn == item[3].ssn)
        all_fields = set(item[0]._fields + item[1]._fields + item[2]._fields + item[3]._fields)
        Data = namedtuple('Data', sorted(all_fields))

        keyword_args = {x: None for x in all_fields}
        for sub_item in item:
            for attr_name in sub_item._fields:
                keyword_args[attr_name] = getattr(sub_item, attr_name)
        yield Data(**keyword_args)


def current_records():
    """
    Goal 3
    Next, you want to identify any stale records, where stale simply means the record has not been updated since 3/1/2017
    (e.g. last update date < 3/1/2017). Create an iterator that only contains current records (i.e. not stale) based on
    the last_updated field from the status_update file.

    :return: a generator
    """
    all_records = full_record()

    for record in all_records:
        if record.last_updated >= datetime(2017, 3, 1):
            yield record


def find_largest_group_car_makes():
    """
    Goal 4
    Find the largest group of car makes for each gender.
    Possibly more than one such group per gender exists (equal sizes).

    :return: a dictionary that lists down the most popular car brand for each gender
    """
    popular_car_by_gender = {'Male': {}, 'Female': {}}
    for record in full_record():
        if record.vehicle_make in popular_car_by_gender[record.gender]:
            popular_car_by_gender[record.gender][record.vehicle_make] += 1
        else:
            popular_car_by_gender[record.gender][record.vehicle_make] = 1

    for gender in popular_car_by_gender:
        car_dict = popular_car_by_gender[gender]
        popular_cars_sorted = sorted(car_dict.keys(), key=lambda x: car_dict[x], reverse=True)
        popularity_count = car_dict[popular_cars_sorted[0]]
        popular_car_by_gender[gender] = {x: car_dict[x] for x in popular_cars_sorted if car_dict[x] == popularity_count}

    return popular_car_by_gender


if __name__ == '__main__':
    print(find_largest_group_car_makes())
