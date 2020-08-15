import random
import string

from enum import Enum
class Case(Enum):
    UPPER = 1
    LOWER = 2
    MIXED = 3

class Datagenerator(object):
    states = ['AL','AS','AR','AK','CA','CO','CN','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NJ','NH','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VM','VA','WA','WV','WI','WY']
    cities = ['Oakland','Three Oaks','Paradise','Hell','Concepcion', 'Newville', 'Jamestown']
    first_names = ['Michael','Paul','Amy','Cheryl','Randy','Becky','Vicky','David','Heidi','Richard','Joseph','Patricia','Foster','Madison','Keegan','Yvonne','Elizabeth']
    last_names = ['Anderson','Amherst','Baines','Carlson','De Jong','Everson','Furman','Garfield','Haynes','Isaacs','Jackson','Klopper','Lamb','Martin','Nieman','O''Doole','Prince','Smith','Quayle','Rhodes','Stark','Thomas','Uhura','Vulcan','Williams','Xavier','Yeoman','Zane']
    street_names = ['Pine','Oak','Main','Maple']
    street_types = ['St.','Dr.','Ave.','Rd.']

    @classmethod
    def state(cls):
        """Returns a random state code from states"""
        random.shuffle(cls.states)
        return cls.states[0]

    @classmethod
    def city(cls):
        """Returns a random city from cities"""
        random.shuffle(cls.cities)
        return cls.cities[0]

    @classmethod
    def first_name(cls):
        """Returns a random element from first_names"""
        random.shuffle(cls.first_names)
        return cls.first_names[0]

    @classmethod
    def last_name(cls):
        """Returns a random element from last_names"""
        random.shuffle(cls.last_names)
        return cls.last_names[0]
        
    @classmethod
    def street_name(cls):
        """Returns a random element from street_names"""
        random.shuffle(cls.street_names)
        return cls.street_names[0]

    @classmethod
    def street_type(cls):
        """Returns a random element from street_types"""
        random.shuffle(cls.street_types)
        return cls.street_types[0]

    
    @classmethod
    def alpha(cls, length, case=Case.UPPER):
        """Returns alphabetic string of length characters"""
        result = ""
        if length <= 0:
            return result
        
        alphasets = {
                    Case.UPPER: string.ascii_uppercase,
                    Case.LOWER: string.ascii_lowercase,
                    Case.MIXED: string.ascii_letters,
                   }
        
        alphaset = alphasets[case]

        for _ in range(length):
            result += alphaset[random.randint(0, len(alphaset) - 1)]

        return result

    @classmethod
    def numeric(cls, length):
        """Returns numeric string of length characters"""
        result = ""
        if length <= 0:
            return result

        for _ in range(length):
            result += "%d" % random.randint(0,10)
        
        return result
    
    @classmethod
    def alphanum(cls, length, case=Case.UPPER):
        """Returns alphanumeric string of length characters"""
        result = ""

        if length <= 0:
            return result
        
        for _ in range(length):
            switch = random.randint(0,2)
            if switch == 0:
                result += cls.numeric(1)
            else:
                result += cls.alpha(1, case)

        return result