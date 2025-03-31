# 7. Конвертер различных величин (американская система, старорусская, СИ).

import unittest
from converter import Converter

class TestConverterCreation(unittest.TestCase):
  def test_converter_instance(self):
    converter = Converter()
    self.assertIsNotNone(converter)

class TestLengthConversion(unittest.TestCase):
  def test_centimeters_to_inches(self):
    converter = Converter()
    result = converter.convert_length(10, 'centimeters', 'inches')
    self.assertAlmostEqual(result, 3.93701, 4, "Неточность в переводе 10 см в дюймы!")
  
  def test_centimeters_to_meters(self):
    converter = Converter()
    result = converter.convert_length(100, 'centimeters', 'meters')
    self.assertAlmostEqual(result, 1, 4, "Неточность в переводе 100 см в м!")

  def test_other_сonversion(self):
    converter = Converter()
    
    result = converter.convert_length(1, 'meters', 'centimeters')
    self.assertAlmostEqual(result, 100, 4, "Неточность в переводе 1 м в см!")

    result = converter.convert_length(1, 'meters', 'inches')
    self.assertAlmostEqual(result, 39.3701, 4, "Неточность в переводе 1 м в дюймы!")

    result = converter.convert_length(1, 'inches', 'centimeters')
    self.assertAlmostEqual(result, 2.54, 4, "Неточность в переводе 1 дюйма в см!")

  def test_other_units(self):
    converter = Converter()

    result = converter.convert_length(1, 'kilometers', 'meters')
    self.assertAlmostEqual(result, 1000, 4, "Ошибка в переводе 1 км в м!")
    
    result = converter.convert_length(1, 'meters', 'millimeter')
    self.assertAlmostEqual(result, 1000, 4, "Ошибка в переводе 1 км в м!")

if __name__ == '__main__':
  unittest.main()