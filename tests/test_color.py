import unittest
from src.color import Color

class TestColor(unittest.TestCase):
    def test_rgb_conversion(self):
        color = Color("#AABBCC")
        self.assertEqual(color.get_rgb(), (170, 187, 204))

    def test_brightness_calculation(self):
        black = Color("#000000")
        white = Color("#FFFFFF")
        self.assertGreater(white.get_brightness(), black.get_brightness())

    def test_different_brightness(self):
        color1 = Color("#AABBCC")
        color2 = Color("#123456")
        self.assertNotEqual(color1.get_brightness(), color2.get_brightness())
        
    def test_invalid_length_too_short(self):
        color = None
        try:
            color = Color("#FFF")
        except ValueError:
            pass
        self.assertIsNone(color)

    def test_invalid_length_too_long(self):
        color = None
        try:
            color = Color("#AABBCCDD")
        except ValueError:
            pass
        self.assertIsNone(color)

    def test_missing_hash(self):
        color = None
        try:
            color = Color("AABBCC")
        except ValueError:
            pass
        self.assertIsNone(color)

    def test_invalid_characters(self):
        color1 = None
        color2 = None
        try:
            color1 = Color("#GGHHII")
        except ValueError:
            pass
        try:
            color2 = Color("#12345G")
        except ValueError:
            pass
        self.assertIsNone(color1)
        self.assertIsNone(color2)

    def test_empty_string(self):
        color = None
        try:
            color = Color("")
        except ValueError:
            pass
        self.assertIsNone(color)

    def test_none_input(self):
        color = None
        try:
            color = Color(None)
        except ValueError:
            pass
        self.assertIsNone(color)

if __name__ == "__main__":
    unittest.main()
