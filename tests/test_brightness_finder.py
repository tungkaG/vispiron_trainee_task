import unittest
import src
from src.brightest_finder import BrightestColorFinder

class TestBrightestFinder(unittest.TestCase):
    def test_find_brightest(self):
        colors = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
        brightest = BrightestColorFinder.find_brightest(colors)
        self.assertEqual(brightest.hex_value, "#FFFFFF")

    def test_black_vs_red(self):
        colors = ["#000000", "#FF0000"]
        brightest = BrightestColorFinder.find_brightest(colors)
        self.assertEqual(brightest.hex_value, "#FF0000")

    def test_single_color(self):
        colors = ["#123456"]
        brightest = BrightestColorFinder.find_brightest(colors)
        self.assertEqual(brightest.hex_value, "#123456")

    def test_all_same_color(self):
        colors = ["#ABCDEF", "#ABCDEF", "#ABCDEF"]
        brightest = BrightestColorFinder.find_brightest(colors)
        self.assertEqual(brightest.hex_value, "#ABCDEF")  

    def test_empty_list(self):
        colors = []
        brightest = BrightestColorFinder.find_brightest(colors)
        self.assertIsNone(brightest)  
if __name__ == "__main__":
    unittest.main()
