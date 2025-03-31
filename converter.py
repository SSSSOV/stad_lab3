class Converter:
  LENGTH_COEFFS = {
    # american system
    'inches': 0.0254,
    'foots':0.3048,
    'yards':0.9144,
    'miles':1609.34,
    # international system
    'centimeters': 0.01,
    'meters': 1.0,
    'kilometers': 1000,
    'millimeters': 0.001,
    # old-russian system
    'arshins': 0.7112,
    'fathoms': 2.1336,
    'versts': 1066.8,
  }
  TIME_COEFFS = {
    'microseconds': 0.000001,
    'milliseconds': 0.001,
    'seconds': 1,
    'minutes': 60,
    'hours': 3600,
    'days': 86400,
    'weeks': 604800,
    'months': 2.628e+6,
    'years': 3.154e+7,
  }

  def __init__(self):
    pass

  def convert_length(self, value, from_unit, to_unit):
    return value * self.LENGTH_COEFFS[from_unit] / self.LENGTH_COEFFS[to_unit]
  
  def convert_time(self, value, from_unit, to_unit):
    return value * self.TIME_COEFFS[from_unit] / self.TIME_COEFFS[to_unit]