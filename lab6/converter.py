from math import isclose
CONVERTER = {'KK': lambda t: t,
             'KC': lambda t: t - 273.15,
             'KF': lambda t: (t - 273.15) * 9/5 + 32,
             }


class Temperature:
    def __init__(self, temperature=0, unit='K'):
