# 7. Конвертер различных величин (американская система, старорусская, СИ).

import unittest
from converter import Converter

class TestConverterCreation(unittest.TestCase):
  def test_converter_instance(self):
    converter = Converter()
    self.assertIsNotNone(converter)

class TestLengthConversion(unittest.TestCase):
  # 1 см = 0.393701 дюйма
  def test_centimeters_to_inches(self):
    converter = Converter()
    result = converter.convert_length(10, 'centimeters', 'inches')
    self.assertAlmostEqual(result, 3.93701, 5, "Неточность в переводе 10 см в дюймы!")
  
  def test_centimeters_to_meters(self):
    converter = Converter()
    result = converter.convert_length(100, 'centimeters', 'meters')
    self.assertAlmostEqual(result, 1, 5, "Неточность в переводе 100 см в м!")

  def test_other_сonversion(self):
    converter = Converter()
    
    result = converter.convert_length(1, 'meters', 'centimeters')
    self.assertAlmostEqual(result, 100, 5, "Неточность в переводе 1 м в см!")

    result = converter.convert_length(1, 'meters', 'inches')
    self.assertAlmostEqual(result, 39.3701, 5, "Неточность в переводе 1 м в дюймы!")

    result = converter.convert_length(1, 'inches', 'centimeters')
    self.assertAlmostEqual(result, 2.54, 5, "Неточность в переводе 1 дюйма в см!")

if __name__ == '__main__':
  unittest.main()