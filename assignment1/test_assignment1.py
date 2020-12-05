import unittest
from assignment1.assignment1 import *
import types


class TestAssignment1(unittest.TestCase):
    def test_iterator(self):
        """
        Test the return types for the Generators
        :return:
        """
        isinstance(employment(), types.GeneratorType)
        isinstance(personal_info(), types.GeneratorType)
        isinstance(update_status(), types.GeneratorType)
        isinstance(vehicles(), types.GeneratorType)

    def test_return_type(self):
        """
        Test the named tuple representation of a record yielded by the generator.
        :return:
        """
        assert str(next(employment())) == "Employment(employer='Stiedemann-Bailey', " \
                                          "department='Research and Development', " \
                                          "employee_id='29-0890771', ssn='100-53-9824')"

        assert str(next(personal_info())) == "Info(ssn='100-53-9824', first_name='Sebastiano', last_name='Tester', " \
                                             "gender='Male', language='Icelandic')"

        assert str(next(update_status())) == "Update_Status(ssn='100-53-9824', " \
                                             "last_updated=datetime.datetime(2017, 10, 7, 0, 14, 42), " \
                                             "created=datetime.datetime(2016, 1, 24, 21, 19, 30))"

        assert str(next(vehicles())) == "Vehicles(ssn='100-53-9824', vehicle_make='Oldsmobile', " \
                                        "vehicle_model='Bravada', model_year=1993)"

    def test_combined_iterator(self):
        """
        Test the combined record format
        :return:
        """
        isinstance(full_record(), types.GeneratorType)
        assert str(next(full_record())) == "Data(created=datetime.datetime(2016, 1, 24, 21, 19, 30), " \
                                           "department='Research and Development', employee_id='29-0890771', " \
                                           "employer='Stiedemann-Bailey', first_name='Sebastiano', gender='Male', " \
                                           "language='Icelandic', last_name='Tester', " \
                                           "last_updated=datetime.datetime(2017, 10, 7, 0, 14, 42), " \
                                           "model_year=1993, ssn='100-53-9824', vehicle_make='Oldsmobile', " \
                                           "vehicle_model='Bravada')"

    def test_current_records(self):
        """
        Test the method to validate the current records
        :return:
        """
        assert str(next(current_records()).last_updated) == "2017-10-07 00:14:42"

    def test_popular_car(self):
        """
        Test the method to check the output of the most popular car by make for each gender
        :return:
        """
        assert str(find_largest_group_car_makes()) == "{'Male': {'Ford': 44}, 'Female': {'Ford': 48, 'Chevrolet': 48}}"


if __name__ == '__main__':
    unittest.main()
