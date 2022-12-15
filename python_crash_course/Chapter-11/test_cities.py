"""Test for city_functions.py."""
import unittest

from city_functions import formatted_city


class NamesTestCase(unittest.TestCase):
    """Test for city_functions.py"""

    def test_city_country(self):
        formatted_name = formatted_city('sofia', 'bulgaria')
        self.assertEqual(formatted_name, 'Sofia, Bulgaria')

    def test_city_country_population(self):
        formatted_name = formatted_city('sofia', 'bulgaria', 5000000)
        self.assertEqual(formatted_name, 'Sofia, Bulgaria - Population 5000000')


if __name__ == '__main__':
    unittest.main()
