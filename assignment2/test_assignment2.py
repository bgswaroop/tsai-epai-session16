import unittest
from assignment2.assignment2 import *
from pathlib import Path


class TestAssignment2(unittest.TestCase):
    def test_context_manager(self):
        """
        Test the class ContextManager
        :return:
        """
        with ContextManager(Path(__file__).parent.joinpath('data/cars.csv')) as cm:
            data_row = next(cm)

        assert str(data_row) == "Header(Car='Chevrolet Chevelle Malibu', MPG='18.0', Cylinders='8', " \
                                "Displacement='307.0', Horsepower='130.0', Weight='3504.', Acceleration='12.0', " \
                                "Model='70', Origin='US')"

    def test_inbuilt_context_manager(self):
        """
        Test the method decorated with inbuilt context manager
        :return:
        """
        with read_csv(Path(__file__).parent.joinpath('data/personal_info.csv')) as cm:
            data_row = next(cm)

        assert str(data_row) == "Header(ssn='100-53-9824', first_name='Sebastiano', last_name='Tester', " \
                                "gender='Male', language='Icelandic')"


if __name__ == '__main__':
    unittest.main()
