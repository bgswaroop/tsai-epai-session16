# EPAi session16 assignment
---

The following requirements need to be met to successfully run the code : 
Dependencies  :   python > = 3.9 \
Python packages  :   refer to requirements.txt

---
## Session16 objectives
This assignment, helps to code the concepts that are learnt in the session 16 of the EPAi module. 
In particular, this assignment focuses on the following topics  : 
 - Chaining and Teeing
 - Mapping and Reducing
 - Zipping
 - Context Managers
 - Lazy Iterators
 - Usage
 - Generators and Context Managers
 - Context Manager Decorator
 
---

The test cases can be executed by executing _pytest_, from python shell

---
## Assignment 1
### Functions

**read_csv(file_name)**

    A generator that reads one line at a time from the csv file
     : param file_name : 
     : return :  generator

**personal_info()**

    Generator to read the personal_info csv file
     : return : 

**vehicles()**

    Generator to read the vehicles.csv file
     : return : 

**employment()**

    Generator to read the employment.csv file
     : return : 

**update_status()**

    Generator to read the update_status.csv file
     : return : 

**date_formatter(x)**


**full_record()**

    Goal 2
    Create a single iterable that combines all the columns from all the iterators.
    The iterable should yield named tuples containing all the columns. Make sure that the SSN's across the files match!
    All the files are guaranteed to be in SSN sort order, and every SSN is unique, and every SSN appears in every file.
    Make sure the SSN is not repeated 4 times - one time per row is enough!

    Generator to read the data from all the csv files, and combine into a single record
     : return : 

**current_records()**

    Goal 3
    Next, you want to identify any stale records, where stale simply means the record has not been updated since 3/1/2017
    (e.g. last update date < 3/1/2017). Create an iterator that only contains current records (i.e. not stale) based on
    the last_updated field from the status_update file.

     : return :  a generator

**find_largest_group_car_makes()**

    Goal 4
    Find the largest group of car makes for each gender.
    Possibly more than one such group per gender exists (equal sizes).

     : return :  a dictionary that lists down the most popular car brand for each gender

### Unit Tests

**test_iterator(self)**

        Test the return types for the Generators
         : return : 

**test_return_type(self)**

        Test the named tuple representation of a record yielded by the generator.
         : return : 

**test_combined_iterator(self)**

        Test the combined record format
         : return : 

**test_current_records(self)**

        Test the method to validate the current records
         : return : 

**test_popular_car(self)**

        Test the method to check the output of the most popular car by make for each gender
         : return : 

___
## Assignment 2
### Functions

**__init__(self, file_name)**


**__enter__(self)**

        Setting up of the context manager
         : return :  a generator

**__exit__(self, exc_type, exc_val, exc_tb)**

        Exiting the context manager
         : param exc_type : 
         : param exc_val : 
         : param exc_tb : 
         : return :  bool value, False indicates to throw the exception, True consumes the exception

**read_csv(file_name)**

    Goal 2
    The goal is to reproduce the work you did in Goal 1, but using a generator function and the contextlib
    contextmanager decorator.

     : param file_name : 
     : return :  a generator that generates (lazily) each row from the csv file

**generator()**


### Unit Tests

**test_context_manager(self)**

        Test the class ContextManager
         : return : 

**test_inbuilt_context_manager(self)**

        Test the method decorated with inbuilt context manager
         : return : 

 