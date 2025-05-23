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

  def test_other_length_units_of_IS(self):
    converter = Converter()

    result = converter.convert_length(1, 'kilometers', 'meters')
    self.assertAlmostEqual(result, 1000, 4, "Ошибка в переводе 1 км в м!")

    result = converter.convert_length(1, 'meters', 'millimeters')
    self.assertAlmostEqual(result, 1000, 4, "Ошибка в переводе 1 км в м!")

  def test_length_units_of_other_systems(self):
    converter = Converter()

    # american
    result = converter.convert_length(1, 'meters', 'inches')
    self.assertAlmostEqual(result, 39.3701, 4, "Ошибка в переводе 1 meter в inch!")

    result = converter.convert_length(1, 'meters', 'foots')
    self.assertAlmostEqual(result, 3.2808, 4, "Ошибка в переводе 1 meter в foot!")

    result = converter.convert_length(1, 'meters', 'yards')
    self.assertAlmostEqual(result, 1.0936, 4, "Ошибка в переводе 1 meter в yard!")

    result = converter.convert_length(1, 'meters', 'miles')
    self.assertAlmostEqual(result, 0.0006214, 4, "Ошибка в переводе 1 meter в mile!")

    # old-russian
    result = converter.convert_length(1, 'meters', 'arshins')
    self.assertAlmostEqual(result, 1.406074, 4, "Ошибка в переводе 1 meter в arshins!")

    result = converter.convert_length(1, 'meters', 'fathoms')
    self.assertAlmostEqual(result, 0.46869141, 4, "Ошибка в переводе 1 meter в fathoms!")

    result = converter.convert_length(1, 'meters', 'versts')
    self.assertAlmostEqual(result, 0.00094, 4, "Ошибка в переводе 1 meter в versts!")

class TestTimeConversion(unittest.TestCase):
  def test_time_conversion(self):
    converter = Converter()

    result = converter.convert_time(1, 'minutes', 'seconds')
    self.assertAlmostEqual(result, 60, 4, "Ошибка в переводе 1 minute в seconds!")

    result = converter.convert_time(1, 'hours', 'seconds')
    self.assertAlmostEqual(result, 3600, 4, "Ошибка в переводе 1 hour в seconds!")

    result = converter.convert_time(1, 'days', 'seconds')
    self.assertAlmostEqual(result, 86400, 4, "Ошибка в переводе 1 day в seconds!")

    result = converter.convert_time(1, 'milliseconds', 'seconds')
    self.assertAlmostEqual(result, 0.001, 4, "Ошибка в переводе 1 millisecond в seconds!")

    result = converter.convert_time(1, 'microseconds', 'seconds')
    self.assertAlmostEqual(result, 1e-6, 4, "Ошибка в переводе 1 microsecond в seconds!")

    result = converter.convert_time(1, 'weeks', 'seconds')
    self.assertAlmostEqual(result, 604800, 4, "Ошибка в переводе 1 week в seconds!")

    result = converter.convert_time(1, 'months', 'seconds')
    self.assertAlmostEqual(result, 2.628e+6, 4, "Ошибка в переводе 1 month в seconds!")

    result = converter.convert_time(1, 'years', 'seconds')
    self.assertAlmostEqual(result, 3.154e+7, 4, "Ошибка в переводе 1 year в seconds!")

    result = converter.convert_time(1, 'years', 'months')
    self.assertAlmostEqual(result, 12, 2, "Ошибка в переводе 1 year в months!")

    result = converter.convert_time(1, 'days', 'hours')
    self.assertAlmostEqual(result, 24, 2, "Ошибка в переводе 1 day в hours!")


if __name__ == '__main__':
  unittest.main()