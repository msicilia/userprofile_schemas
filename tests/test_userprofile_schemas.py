#!/usr/bin/env python

"""Tests for `userprofile_schemas` package."""


import unittest

from userprofile_schemas import  extract_schema_from_csvs


class TestUserprofile_schemas(unittest.TestCase):
    """Tests for `userprofile_schemas` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        pass

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_get_schema_from_csv(self):
        """Tests getting the schema from a single CSV."""
        schema = extract_schema_from_csvs('tests/Retail.OrdersReturned.2.csv')
        with open('tests/schema_single.txt') as x: f = x.read()
        assert(schema.strip()==f.strip())


    def test_get_schema_from_csv_folder(self):
        """Tests getting the schema from a folder with CSVs."""
        schema = extract_schema_from_csvs('tests/somefiles')
        with open('tests/schema_folder.txt') as x: f = x.read()
        assert(schema.strip()==f.strip())
     
if __name__ == '__main__':
    unittest.main()