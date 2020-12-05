from contextlib import contextmanager
from collections import namedtuple
import csv


# Goal 1
# For this goal, you are given a number of CSV files, each of which have their first row with the field name.
# You goal is to create a context manager that you can use to produce the data from each file in a named tuple with
# field names corresponding to the header row field names.
# You should use the csv module's reader function to help with parsing the data.
# Your context manager should be generic in the sense that it should just need the file name, no other configuration
# or hardcoded functionality is required. You do not need to worry about data types for this goal -
# just return every field as a string.
# In addition, your context manager should produce lazy iterators.
# Implement this using a class that implements the context manager protocol

class ContextManager:

    def __init__(self, file_name):
        self.file_name = file_name
        self.Header = None
        self.file_pointer = None

    def __enter__(self):
        """
        Setting up of the context manager
        :return: a generator
        """
        with open(self.file_name, 'r') as f:
            header_row = next(f)
            if ',' in header_row:
                delimiter = ','
            elif ';' in header_row:
                delimiter = ';'
            else:
                raise AssertionError('No valid delimiters found in the CSV file')
            header_row = [x.strip() for x in header_row.split(delimiter)]

            self.file_pointer = csv.reader(f, delimiter=delimiter, quotechar='"')
            self.Header = namedtuple('Header', header_row)

            for row in self.file_pointer:
                yield self.Header(*row)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exiting the context manager
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return: bool value, False indicates to throw the exception, True consumes the exception
        """
        return False


@contextmanager
def read_csv(file_name):
    """
    Goal 2
    The goal is to reproduce the work you did in Goal 1, but using a generator function and the contextlib
    contextmanager decorator.

    :param file_name:
    :return: a generator that generates (lazily) each row from the csv file
    """

    def generator():
        with open(file_name, 'r') as f:
            header_row = next(f)
            if ',' in header_row:
                delimiter = ','
            elif ';' in header_row:
                delimiter = ';'
            else:
                raise AssertionError('No valid delimiters found in the CSV file')
            header_row = [x.strip() for x in header_row.split(delimiter)]

            file_pointer = csv.reader(f, delimiter=delimiter, quotechar='"')
            Header = namedtuple('Header', header_row)

            for row in file_pointer:
                yield Header(*row)

    try:
        # Run some code here (similar to __enter__)
        print('Running code at the beginning of the context')
        yield generator()
    except Exception as e:
        # Catch exceptions similar to __exit__
        print('Caught exception: ', e)
        print('Traceback: ', e.__traceback__)  # the attribute __traceback__ contains the traceback object
        raise e  # This is similar to return False in __exit__
    finally:
        # Run some code here (Similar to __exit__)
        print('Running code at the end of the context')


if __name__ == '__main__':
    pass
    # from itertools import islice
    #
    # with ContextManager(Path(__file__).parent.joinpath('data/cars.csv')) as cm1:
    #     for data_row in islice(cm1, 10):
    #         print(data_row)
    #
    # with read_csv(Path(__file__).parent.joinpath('data/personal_info.csv')) as cm2:
    #     for data_row in islice(cm2, 10):
    #         print(data_row)
