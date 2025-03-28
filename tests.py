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

if __name__ == '__main__':
  unittest.main()