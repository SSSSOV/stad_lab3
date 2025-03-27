import unittest
from converter import Converter

class TestConverterCreation(unittest.TestCase):
  def test_converter_instance(self):
    converter = Converter()
    self.assertIsNotNone(converter)

if __name__ == '__main__':
  unittest.main()