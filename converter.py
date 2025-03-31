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
    'millimeter': 0.001,
    # old-russian system
    'arshins': 0.7112,
    'fathoms': 2.1336,
    'versts': 1066.8,
  }

  def __init__(self):
    pass

  def convert_length(self, value, from_unit, to_unit):
    return value * self.LENGTH_COEFFS[from_unit] / self.LENGTH_COEFFS[to_unit]