from src.brightest_finder import BrightestColorFinder
from src.color_finder import ColorFinder
import requests

if __name__ == "__main__":
    colors = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
    brightest = BrightestColorFinder.find_brightest(colors)
    r, g, b = brightest.get_rgb()
    brightest_name = ColorFinder.find_closest_color([r, g, b])
    print(f"The brightest color is: {brightest.hex_value} (r={r}, g={g}, b={b}), called {brightest_name}.")