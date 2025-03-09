import math
import requests

class ColorFinder:
    @staticmethod
    def euclidean_distance(rgb1, rgb2):
        """Calculate the Euclidean distance between two RGB values."""
        return math.sqrt((rgb1[0] - rgb2[0])**2 + (rgb1[1] - rgb2[1])**2 + (rgb1[2] - rgb2[2])**2)

    @staticmethod
    def find_closest_color(input_rgb):
        """Find the closest color from the list based on the input hex value."""
        if not isinstance(input_rgb, list):
            raise TypeError("Input RGB must be a tuple.")
        if len(input_rgb) != 3:
            raise ValueError("Input RGB must be a tuple of length 3.")
        if any(val < 0 or val > 255 for val in input_rgb):
            raise ValueError("RGB values must be in the range [0, 255].")
        
        url = "https://csscolorsapi.com/api/colors"
        response = requests.get(url)
        data = response.json()
        colors = data['colors']
        
        closest_color_name = None
        closest_distance = float('inf')

        for color in colors:
            color_rgb = list(map(int, color['rgb'].split(','))) # Convert list of strings to list of integers
            distance = ColorFinder.euclidean_distance(input_rgb, color_rgb)
            if distance < closest_distance:
                closest_distance = distance
                closest_color_name = color['name']

        return closest_color_name