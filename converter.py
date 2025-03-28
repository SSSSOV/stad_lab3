class Converter:
  def __init__(self):
    pass

  def convert_length(self, value, from_unit, to_unit):
    if(from_unit == 'centimeters' and to_unit == 'inches'):
      return value / 2.54
    if(from_unit == 'centimeters' and to_unit == 'meters'):
      return value / 100
    else: return -1