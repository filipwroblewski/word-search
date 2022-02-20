import unittest
from finder import Finder


class TestFinder(unittest.TestCase):

	def test_lrrf(self):
		word_search = Finder(['ab', 'de'], 'ab de')
		self.assertEqual(word_search.lrrf(), ['ab', 'de'])

	def test_rlrf(self):
		word_search = Finder(['ab', 'de'], 'ba ed')
		self.assertEqual(word_search.rlrf(), ['ab', 'de'])

	def test_udcf(self):
		word_search = Finder(['ab', 'de'], 'ad be')
		self.assertEqual(word_search.udcf(), ['ad', 'be'])

	def test_ducf(self):
		word_search = Finder(['ab', 'de'], 'da eb')
		self.assertEqual(word_search.ducf(), ['ad', 'be'])


if __name__ == '__main__':
	unittest.main()