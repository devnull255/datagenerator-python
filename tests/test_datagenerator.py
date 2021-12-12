from datagenerator import Datagenerator, Case
import unittest
import logging
import string
LOG_FORMAT = "%(filename)s|%(funcName)s|%(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
class TestDatagenerator(unittest.TestCase):
    def test_datagenerator_state(self):
        """
        Ensures state is a valid state from Datagenerator.states

        """
        aState = Datagenerator.state()
        logging.info("state: %s" % aState)
        self.assertIn(aState, Datagenerator.states)
 
    def test_datagenerator_city(self):
        """
        Ensures city is valid from Datagenerator.cities
        """
        aCity = Datagenerator.city()
        logging.info("city: %s" % aCity)
        self.assertIn(aCity, Datagenerator.cities)

    def test_datagenerator_first_name(self):
        """
        Ensures first name is valid from Datagenerator.first_names
        """
        aFirstName = Datagenerator.first_name()
        logging.info("first name: %s" % aFirstName)
        self.assertIn(aFirstName, Datagenerator.first_names)

    def test_datagenerator_last_name(self):
        """
        Ensures last name is valid from Datagenerator.last_names)
        """
        aLastName = Datagenerator.last_name()
        logging.info("last name: %s" % aLastName)
        self.assertIn(aLastName, Datagenerator.last_names)

    def test_datagenerator_street_name(self):
        """
        Ensures street_name is valid from Datagenerator.street_names
        """
        aStreetName = Datagenerator.street_name()
        logging.info("street name: %s" % aStreetName)
        self.assertIn(aStreetName, Datagenerator.street_names)

    def test_datagenerator_street_type(self):
        """
        Ensures street_type generates valid street_type from 
        Datagenerator.street_types
        """
        aStreetType = Datagenerator.street_type()
        logging.info("street type: %s" % aStreetType)
        self.assertIn(aStreetType, Datagenerator.street_types)

    def test_datagenerator_numeric(self):
        """
         Ensure random string returned by numeric() is numeric and
         of specified size
        """
        aString = Datagenerator.numeric(9)
        logging.info("aString: %s" %  aString)
        self.assertEqual(len(aString), 9)
        self.assertTrue(aString.isnumeric())

    def test_datagenerator_alpha(self):
        """
        Ensure random string returned by alpha() is of specified length
        and case
        """
        defaultCaseString = Datagenerator.alpha(10) # default case is uppercase
        logging.info("default case string: %s" % defaultCaseString)
        self.assertEqual(len(defaultCaseString), 10)
        self.assertTrue(defaultCaseString.isupper())

        lowerCaseString = Datagenerator.alpha(10, Case.LOWER)
        logging.info("lowercase string: %s" % lowerCaseString)
        self.assertTrue(lowerCaseString.islower())

        upperCaseString = Datagenerator.alpha(10, Case.UPPER)
        logging.info("uppercase string: %s" % upperCaseString)
        self.assertTrue(upperCaseString.isupper())

        mixedCaseString = Datagenerator.alpha(10, Case.MIXED)
        logging.info("mixed case string: %s" % mixedCaseString)
        self.assertFalse(mixedCaseString.islower() or mixedCaseString.isupper())
        

    def test_datagenerator_alphanum(self):
        """
        Ensure random string returned by alphanum() is of specified length
        and has numbers and/or letters
        """
        alphanumString = Datagenerator.alphanum(5)
        logging.info("alphanumString: %s" % alphanumString)
        alphanums = set(string.ascii_letters).union(set(string.digits))
        self.assertTrue(set(alphanumString).issubset(alphanums))
