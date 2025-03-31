class Converter:
  LENGTH_COEFFS = {
    'inches': 0.0254,
    'centimeters': 0.01,
    'meters': 1.0,
    'kilometers': 1000,
    'millimeter': 0.001
  }

  def __init__(self):
    pass

  def convert_length(self, value, from_unit, to_unit):
    return value * self.LENGTH_COEFFS[from_unit] / self.LENGTH_COEFFS[to_unit]