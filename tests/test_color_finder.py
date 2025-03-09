import unittest
import src
from src.color_finder import ColorFinder

class TestBrightestFinder(unittest.TestCase):
    def test_close_to_red(self):
        color = ColorFinder.find_closest_color([255, 1, 0])
        self.assertEqual(color, "Red")
        
    def test_exact_white(self):
        color = ColorFinder.find_closest_color([255, 255, 255])
        self.assertEqual(color, "White")
        
    def test_invalid_negative_values(self):
        try:
            ColorFinder.find_closest_color([-1, 0, 0])
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised for negative RGB value.")

    def test_tuple_invalid_number_of_elements(self):
        try:
            ColorFinder.find_closest_color([255, 255]) 
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised for tuple with less than three elements.")

        try:
            ColorFinder.find_closest_color([255, 255, 255, 255]) 
        except ValueError:
            pass 
        else:
            self.fail("ValueError not raised for tuple with more than three elements.")

    def test_invalid_type_input(self):
        try:
            ColorFinder.find_closest_color("255,255,255") 
        except TypeError:
            pass  
        else:
            self.fail("TypeError not raised for string input.")

    def test_empty_input(self):
        try:
            ColorFinder.find_closest_color([]) 
        except ValueError:
            pass  
        else:
            self.fail("ValueError not raised for empty tuple input.")
            
    def test_euclidean_distance(self):            
        distance = ColorFinder.euclidean_distance([1, 255, 0], [0, 255, 0])
        self.assertEqual(distance, 1)  
        
if __name__ == "__main__":
    unittest.main()