class Converter:
  def __init__(self):
    pass

  def convert_length(self, value, from_unit, to_unit):
    if(from_unit == 'centimeters' and to_unit == 'inches'):
      return value / 2.54